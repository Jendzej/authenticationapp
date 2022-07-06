from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='posts'),
    path('', views.posts, name='posts'),
]
