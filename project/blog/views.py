from django.shortcuts import render

def blog_home(request):
    return render(request, 'index.html')