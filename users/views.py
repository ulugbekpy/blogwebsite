from django.shortcuts import render,redirect
from django.views.generic import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm,PasswordResetForm

# view for registration page
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,f"Registration have been successfully completed for {username}!")
            return redirect('login')
    else:
        form = UserRegisterForm()
        context = {'form': form}
    return render(request,template_name='users/register.html',context=context)

def me(request):
    return render(request,template_name='users/me.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"Your profile info updated successfully!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request,template_name='users/profile.html',context=context)


class UserListView(LoginRequiredMixin,ListView):
    model = Profile
    template_name = 'users/profiles.html'
    context_object_name = 'profiles'
    ordering = '-id'


def password_reset_view(request):
    form = PasswordResetForm()
    