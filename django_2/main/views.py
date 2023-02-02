from django.shortcuts import render
from .models import Blog
from django.views.generic import DetailView
from .forms import TaskForm

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def new(request):
    data = Blog.objects.all()
    return render(request, 'main/new_page.html', {'data': data})

def about(request):
    return render(request, 'main/about.html')

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'main/new_page_detail.html'
    context_object_name = 'blog'

def task(request):
    form = TaskForm()
    data = {
        'form': form
    }
    return render(request, 'main/task.html', data)
