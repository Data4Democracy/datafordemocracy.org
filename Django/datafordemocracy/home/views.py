from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html', {})

def about(request):
    return render(request, 'home/about.html', {})

def projects(request):
    return render(request, 'home/projects.html', {})

def contactus(request):
    return render(request, 'home/contactus.html', {})