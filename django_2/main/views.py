from django.shortcuts import render
from .models import Blog
from django.db import models

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def new(request):
    data = Blog.objects.all()
    return render(request, 'main/new_page.html', {'data': data})

def about(request):
    return render(request, 'main/about.html')

