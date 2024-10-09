from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'address', 'phone']

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    age = forms.IntegerField(required=True)
    address = forms.CharField(max_length=255, required=True)
    phone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'age', 'address', 'phone']

    def save(self, commit=True):
        user = super().save(commit=False)  # Create user without saving to DB yet
        user.email = self.cleaned_data['email']  # Assign the email from the cleaned data
        if commit:
            user.save()  # Save user first to get a primary key
            UserProfile.objects.create(
                user=user,
                age=self.cleaned_data['age'],
                address=self.cleaned_data['address'],
                phone=self.cleaned_data['phone']
            )
        return user
