from django.shortcuts import render

# This view is for main page
def mainpage(request):
    return render(request,template_name='app/index.html')