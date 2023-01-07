from django.shortcuts import render
from .models import Post

# This view is for main page
def mainpage(request):
    posts = Post.objects.all()
    ctx = {'posts':posts}
    return render(request,template_name='app/index.html',context=ctx)