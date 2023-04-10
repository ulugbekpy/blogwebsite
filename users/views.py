from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile, Post
from django.contrib.auth.models import User
from .forms import (UserRegisterForm1, UserRegisterForm2,
                    ProfileUpdateForm, UserUpdateForm,
                    PasswordResetForm)


def registration1(request):
    if request.method == 'POST':
        form = UserRegisterForm1(request.POST)
        if form.is_valid():
            request.session['registration_form'] = form.cleaned_data
            return redirect('step2')
    else:
        form = UserRegisterForm1()
    return render(request, 'users/registration1.html', {'form': form})


def registration2(request):
    if request.method == 'POST':
        form = UserRegisterForm2(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=request.session['registration_form']['username'],
                password=request.session['registration_form']['password'],
                email=request.session['registration_form']['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            user.set_password(request.session['registration_form']['password'])
            user.profile.shortdesc = form.cleaned_data['shortdesc']
            user.save()
            return redirect('login')
    else:
        form = UserRegisterForm2()
    return render(request,
                  template_name='users/registration2.html', context={'form': form})


def me(request):
    return render(request, template_name='users/me.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, message="Your profile info updated successfully!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, template_name='users/profile.html', context=context)


class UserListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'users/profiles.html'
    context_object_name = 'profiles'
    ordering = '-id'


def password_reset_view(request):
    form = PasswordResetForm()


def like(request, id):
    Post.objects.filter(pk=id).first().likes += 1
    return HttpResponse('you liked this post')
