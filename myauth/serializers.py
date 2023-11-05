from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from users.models import Player


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Player
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        player = Player(**validated_data)
        player.password = make_password(password)
        player.save()
        return player
