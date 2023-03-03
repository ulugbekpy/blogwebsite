from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile, Post
from django.contrib.auth.models import User
from .forms import (UserRegisterForm1, UserRegisterForm2,
                    ProfileUpdateForm, UserUpdateForm,
                    PasswordResetForm)


def register1(request):
    if request.method == 'POST':
        form = UserRegisterForm1(request.POST)
        if form.is_valid():
            request.session['fn'] = form.cleaned_data['fn']
            return HttpResponseRedirect(reverse_lazy('step2'))

    form = UserRegisterForm1()
    return render(request, 'register1.html', context={'form': form})


def register2(request):
    if request.method == 'POST':
        form = UserRegisterForm2(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['username']
            user = User.objects.create(
                fn=request.session['fn'], username=form.changed_data['username'])
            user.set_password[form.cleaned_data['password']]
            user.save()
            messages.success(
                request, f"Registration successfully finished for {user.username} !")
            return HttpResponseRedirect(reverse_lazy('login'))

    form = UserRegisterForm2()
    return render(request, template_name='register2.html', context={'form': form})
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             username = form.cleaned_data.get('username')
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             messages.success(
#                 request, f"Registration have been successfully completed for {username}!")
#             return redirect('login')
#     else:
#         form = UserRegisterForm()

#     return render(request, template_name='users/register.html', context={'form': form})


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
                request, f"Your profile info updated successfully!")
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
    liked = False
    Post.objects.filter(pk=id).first().likes += 1
    return HttpResponse('you liked this post')


def unlike(request):
    liked = True
