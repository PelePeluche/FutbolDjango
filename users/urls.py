from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.PlayerList.as_view(), name='player-list'),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name='player-detail'),
]
