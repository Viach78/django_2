from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new, name="new_page"),
    path('about/', views.about, name="about"),
    path('new_page/<int:pk>', views.BlogDetailView.as_view(), name="new_page_detail")
]
