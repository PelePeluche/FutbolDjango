from rest_framework import generics, permissions
from .models import Player
from .serializers import PlayerSerializer


class PlayerList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerUpdate(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDelete(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


# class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Player.objects.all()
#     serializer_class = PlayerSerializer
