from django.urls import path
from .views import (
    TentativeMatchList,
    TentativeMatchDetail,
    TentativeMatchUpdate,
    TentativeMatchDelete,
)

urlpatterns = [
    path(
        "tentative-matches/",
        TentativeMatchList.as_view(),
        name="tentative-match-list",
    ),
    path(
        "tentative-matches/<int:pk>/",
        TentativeMatchDetail.as_view(),
        name="tentative-match-detail",
    ),
    path(
        "tentative-matches/<int:pk>/update/",
        TentativeMatchUpdate.as_view(),
        name="tentative-match-update",
    ),
    path(
        "tentative-matches/<int:pk>/delete/",
        TentativeMatchDelete.as_view(),
        name="tentative-match-delete",
    ),
]
