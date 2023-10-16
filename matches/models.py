from django.db import models
from users.models import Player


# Create your models here.
class TentativeMatch(models.Model):
    date = models.DateField()
    registered_players = models.ManyToManyField(Player)
