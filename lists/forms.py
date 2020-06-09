from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as AuthUser
from .models import Profile
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = AuthUser
        fields = ['username','email', 'password1','password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['username', 'email']


