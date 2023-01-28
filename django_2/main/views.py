from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new_page.html')

def about(request):
    return render(request, 'main/about.html')

