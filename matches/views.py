from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TentativeMatch
from .serializers import TentativeMatchSerializer


class TentativeMatchListCreate(generics.ListCreateAPIView):
    queryset = TentativeMatch.objects.all()
    serializer_class = TentativeMatchSerializer


class TentativeMatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TentativeMatch.objects.all()
    serializer_class = TentativeMatchSerializer
