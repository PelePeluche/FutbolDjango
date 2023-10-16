from rest_framework import serializers
from .models import TentativeMatch


class TentativeMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TentativeMatch
        fields = "__all__"
