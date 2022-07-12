"""Posts app urls configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_page, name='posts'),
    path('add/', views.adding_post, name='add'),
    path('edit/<post_id>', views.edit_post, name='edit'),
    path('delete/<post_id>', views.delete_post, name='delete')
]
