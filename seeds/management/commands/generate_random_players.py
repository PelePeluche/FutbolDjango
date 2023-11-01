from django.core.management.base import BaseCommand
from seeds.scripts.players import generate_random_player


class Command(BaseCommand):
    help = "Create random players"

    def add_arguments(self, parser):
        """
        Add arguments to the parser.

        Args:
            parser: The argument parser object.
        """
        parser.add_argument(
            "number_of_players",
            nargs="?",
            default=10,
            type=int,
            help="The number of players to add.",
        )

    def handle(self, *args, **options):
        """
        Handle the creation of players based on the provided number.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
                number_of_players (int): The number of players to create.

        Returns:
            None
        """
        number_of_players = options.get("number_of_players")

        # Iterate over the range of number_of_players
        for _ in range(number_of_players):
            generate_random_player(self)

        # Print success message
        self.stdout.write(self.style.SUCCESS("Successfully created players"))
