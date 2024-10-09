from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm
from .forms import CustomUserCreationForm
from products.models import Product
from django.contrib import messages
from .models import UserProfile

# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! You can now log in.')  # Success message
            login(request, user)  # Log the user in after registration
            return redirect('product_list')  # Redirect to a product list page after registration
        else:
            # Optionally, you can add an error message for overall form errors
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
            return redirect('profile')  # Redirect to the profile page
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })




def home(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'home.html', {'products': products})

