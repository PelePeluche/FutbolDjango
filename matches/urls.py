from django.urls import path
from . import views

urlpatterns = [
    path(
        "tentative-matches/",
        views.TentativeMatchListCreate.as_view(),
        name="tentative-match-list-create",
    ),
    path(
        "tentative-matches/<int:pk>/",
        views.TentativeMatchDetail.as_view(),
        name="tentative-match-detail",
    ),
]
