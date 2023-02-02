from django.shortcuts import render, redirect
from .models import Blog, Task
from django.views.generic import DetailView
from .forms import TaskForm


# Create your views here.

def index(request):
    task_all = Task.objects.order_by('-data')
    return render(request, 'main/index.html', {'task_all': task_all})


class TaskDetailView(DetailView):
    model = Task
    template_name = 'main/task_detail.html'
    context_object_name = 'task'


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
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Запись некорректная'

    form = TaskForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/task.html', data)
