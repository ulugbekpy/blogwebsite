from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm
from django.contrib import messages

# view for registration page
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
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

@login_required
def chat(request):
    return render(request,'users/postboard.html')

