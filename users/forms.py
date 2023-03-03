from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm1(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=100)


class UserRegisterForm2(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.PasswordInput()
    password1 = forms.PasswordInput()

    def clean(self):
        if 'password1' in self.cleaned_data and 'password' in self.cleaned_data and self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError("The password does not match ")
        return self.cleaned_data


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
