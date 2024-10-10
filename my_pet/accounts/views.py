from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, UserProfileForm, CustomUserCreationForm
from products.models import Product
from .models import UserProfile
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User

# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose another one.')
            return render(request, 'registration/register.html', {'form': form})
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists. Please use another one.')
            return render(request, 'registration/register.html', {'form': form})

        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=getattr(request.user, 'userprofile', None))
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')  # Add success message
            return redirect('profile')  # Redirect to the profile page
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=getattr(request.user, 'userprofile', None))

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

# Custom logout view with success message
def custom_logout(request):
    messages.success(request, "You have been logged out successfully.")
    #return auth_views.LogoutView.as_view()(request)
    return redirect('login')

def home(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'home.html', {'products': products})
