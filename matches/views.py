from rest_framework import generics
from .models import TentativeMatch
from .serializers import TentativeMatchSerializer


class TentativeMatchListCreate(generics.ListCreateAPIView):
    queryset = TentativeMatch.objects.all()
    serializer_class = TentativeMatchSerializer


class TentativeMatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TentativeMatch.objects.all()
    serializer_class = TentativeMatchSerializer
