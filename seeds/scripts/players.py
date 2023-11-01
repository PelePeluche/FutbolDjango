from django.utils.timezone import make_aware
from django.db import IntegrityError
from faker import Faker
from users.models import Player


def generate_random_player(self):
    """
    Generate a random player object and create it in the database.
    """
    fake = Faker()

    # Generate random first name
    first_name = fake.first_name()

    # Generate random last name
    last_name = fake.last_name()

    # Generate random username
    username = f"{first_name}_{last_name}_{fake.pyint(min_value=1, max_value=99)}"

    # Generate random email
    email = f"{username}@example.com"

    # Generate random date joined
    date_joined = make_aware(fake.date_time_between(start_date="-1y", end_date="now"))

    # Generate random password
    password = fake.password()

    try:
        # Create a new Player object with the generated data
        Player.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            date_joined=date_joined,
            password=password,
        )
    except IntegrityError as e:
        # Handle IntegrityError exception
        self.stdout.write(
            self.style.ERROR(f"Failed to create player {username}: {str(e)}")
        )
    except Exception as e:
        # Handle other exceptions
        self.stdout.write(
            self.style.ERROR(
                f"An error occurred while creating player {username}: {str(e)}"
            )
        )
