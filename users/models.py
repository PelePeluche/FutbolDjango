from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class Player(AbstractUser):
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    statistics = models.JSONField(null=True, blank=True)
