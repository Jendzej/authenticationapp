""" file to config apps included in this part of application """
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Accounts app configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
