from django.apps import AppConfig


class RngBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rng_base'
    verbose_name = 'База РНГ'
