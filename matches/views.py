from rest_framework import generics, permissions
from .models import TentativeMatch
from .serializers import TentativeMatchSerializer


class TentativeMatchList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = TentativeMatch.objects.all()
    serializer_class = TentativeMatchSerializer


class TentativeMatchDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = TentativeMatch.objects.all()
    serializer_class = TentativeMatchSerializer


class TentativeMatchUpdate(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TentativeMatch.objects.all()
    serializer_class = TentativeMatchSerializer


class TentativeMatchDelete(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TentativeMatch.objects.all()
    serializer_class = TentativeMatchSerializer
