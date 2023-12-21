from django.apps import AppConfig


class AluguelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aluguel'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals
