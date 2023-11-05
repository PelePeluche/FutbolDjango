from django.urls import path
from .views import PlayerDelete, PlayerDetail, PlayerList, PlayerUpdate

urlpatterns = [
    path("players/", PlayerList.as_view(), name="player-list"),
    path("players/<int:pk>/", PlayerDetail.as_view(), name="player-detail"),
    path("players/<int:pk>/update/", PlayerUpdate.as_view(), name="player-update"),
    path("players/<int:pk>/delete/", PlayerDelete.as_view(), name="player-delete"),
]
