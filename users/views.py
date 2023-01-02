from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
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
    return render(request,template_name='users/profile.html')

@login_required
def chat(request):
    return render(request,'users/postboard.html')