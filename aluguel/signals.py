from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Cliente

@receiver(post_save, sender=get_user_model())
def criar_cliente(sender, instance, created, **kwargs):
    if created:
        cliente = Cliente.objects.create(nome=instance.get_full_name(), email=instance.email, user=instance)