from django.utils.timezone import make_aware
from django.db import IntegrityError
from faker import Faker
from matches.models import TentativeMatch
from users.models import Player


def generate_random_tentative_match(self):
    """
    Generate a random tentative match with registered players.
    """
    # Generate fake data
    fake = Faker()

    # Generate a random match date within the last year
    match_date = make_aware(fake.date_time_between(start_date="-1y", end_date="now"))

    # Get the first 14 players registered before the match date
    registered_players = Player.objects.filter(date_joined__lte=match_date).order_by(
        "?"
    )[:14]

    try:
        # Create a new tentative match and associate it with the registered players
        tentative_match = TentativeMatch.objects.create(date=match_date)
        tentative_match.registered_players.set(registered_players)
    except IntegrityError as e:
        # Handle IntegrityError exception
        self.stdout.write(
            self.style.ERROR(f"Failed to create the tentative match: {str(e)}")
        )
    except Exception as e:
        # Handle other exceptions
        self.stdout.write(
            self.style.ERROR(
                f"An error occurred while creating tentative match: {str(e)}"
            )
        )
