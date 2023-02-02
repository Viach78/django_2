from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new_page"),
    path('about/', views.about, name="about"),
    path('new_page/<int:pk>', views.BlogDetailView.as_view(), name="new_page_detail"),
    path('task/', views.task, name="task"),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name="task_detail"),
]
