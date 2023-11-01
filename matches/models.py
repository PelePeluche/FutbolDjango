from django.db import models
from users.models import Player


class TentativeMatch(models.Model):
    date = models.DateTimeField()
    registered_players = models.ManyToManyField(Player, through="PlayerRegistration")


class PlayerRegistration(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tentative_match = models.ForeignKey(TentativeMatch, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
