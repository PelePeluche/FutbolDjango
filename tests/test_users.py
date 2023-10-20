import pytest
from users.models import Player
from users.serializers import PlayerSerializer
from django.contrib.auth.models import AbstractBaseUser


@pytest.mark.django_db
def test_player_create():
    player = Player.objects.create(
        username="testuser",
        email="testuser@example.com",
        password="testpass",
        avatar="path/to/avatar.jpg",
        statistics={"wins": 10, "losses": 5},
    )
    assert player.username == "testuser"
    assert player.email == "testuser@example.com"
    assert player.password == "testpass"
    assert player.avatar == "path/to/avatar.jpg"
    assert player.statistics == {"wins": 10, "losses": 5}


@pytest.mark.django_db
def test_player_nulleable_fields():
    player = Player.objects.create()

    assert str(player.avatar) == ""
    assert player.statistics is None


@pytest.mark.django_db
def test_player_inheritance():
    assert issubclass(Player, AbstractBaseUser)


@pytest.fixture
def test_player_data():
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass",
    }


@pytest.fixture
def test_player(test_player_data):
    return Player.objects.create(**test_player_data)


@pytest.mark.django_db
def test_player_serializer_serialization(test_player):
    serializer = PlayerSerializer(test_player)
    data = serializer.data

    assert "id" in data
    assert data["username"] == test_player.username
    assert data["email"] == test_player.email


@pytest.mark.django_db
def test_player_serializer_deserialization(test_player_data):
    serializer = PlayerSerializer(data=test_player_data)

    assert serializer.is_valid(), serializer.errors
    player = serializer.save()

    assert player.username == test_player_data["username"]
    assert player.email == test_player_data["email"]
