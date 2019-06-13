from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    is_anfitriao = models.BooleanField('anfitriao user', default=False)
    is_acolhido = models.BooleanField('acolhido user', default=False)

class Acolhido(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='acolhido')
    nome = models.CharField(max_length=120)
    contato = models.CharField(max_length=11)
    descricao = models.TextField()
    vagas = models.PositiveIntegerField(default=1)
    achou_moradia = models.BooleanField(default=False)
	# fotinha
    # email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	print('****', created)
	if instance.is_acolhido:
		Acolhido.objects.get_or_create(user = instance)
    
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	print('_-----')	
	# print(instance.internprofile.bio, instance.internprofile.location)
	if instance.is_acolhido:
		instance.acolhido.save()