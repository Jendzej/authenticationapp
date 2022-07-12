"""Posts app urls configuration"""
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.posts_page, name='posts'),
    path('add/', views.adding_post, name='add'),
    path('edit/<post_id>', views.edit_post, name='edit'),
    path('delete/<post_id>', views.delete_post, name='delete'),
    path('pdf/<post_id>', views.get_pdf, name='get_pdf')
]

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
