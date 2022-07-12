"""Posts app admin configuration (registering modules)"""
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.ModelPost)
admin.site.register(models.Comment)
