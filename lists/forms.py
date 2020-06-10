from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib.auth.models import User as AuthUser
from .models import Profile
class UserRegisterForm(UserCreationForm):

    def validate_email(email):
        if AuthUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already taken')
        return email
    email = forms.EmailField(validators=[validate_email])

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

#
# class CustomEmailValidationForm(PasswordResetForm):
#     def validate_email(self):
#             email = self.cleaned_data['email']
#             if not AuthUser.objects.filter(email=email).exists():
#                 raise forms.ValidationError('Invalid email, plz use registered email')
#             return email
#             email = forms.EmailField(validators=[validate_email])


