from django.apps import AppConfig


class APIConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    verbose_name = 'Curriculum Vitae API'