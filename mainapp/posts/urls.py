from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='posts'),
    path('adding/', views.adding_post, name='adding')
]
