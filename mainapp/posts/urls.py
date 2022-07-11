"""Posts app urls configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_page, name='posts'),
    path('add/', views.adding_post, name='add')
]
