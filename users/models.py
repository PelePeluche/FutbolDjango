from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _


# Create your models here.
class Player(AbstractUser):
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    estadisticas = models.JSONField(null=True, blank=True)
