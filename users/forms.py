from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm1(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserRegisterForm2(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    shortdesc = forms.CharField(widget=forms.Textarea)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class PasswordResetForm(forms.Form):
    email = forms.EmailField()
