from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h2>Hello</h2>')

def new(request):
    return HttpResponse('<h1>New page</h1>')
