from django.db import models
from users.models import Player


class TentativeMatch(models.Model):
    date = models.DateField()
    registered_players = models.ManyToManyField(Player)
