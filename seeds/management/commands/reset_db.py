from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
import subprocess


class Command(BaseCommand):
    help = "Reset the database and create a superuser."

    def add_arguments(self, parser):
        """
        Adds arguments to the parser for creating a superuser.

        Args:
            parser (argparse.ArgumentParser): The argument parser object.

        Returns:
            None
        """
        # Add argument for username
        parser.add_argument("--username", type=str, help="Username for the superuser")

        # Add argument for email
        parser.add_argument("--email", type=str, help="Email for the superuser")

        # Add argument for password
        parser.add_argument("--password", type=str, help="Password for the superuser")

    def handle(self, *args, **options):
        # Get the command line options
        username = options.get("username")
        email = options.get("email")
        password = options.get("password")

        try:
            # Drop the existing database
            subprocess.run(
                [
                    "sudo",
                    "-u",
                    "postgres",
                    "psql",
                    "-c",
                    "DROP DATABASE IF EXISTS futbol",
                ]
            )

            # Create a new database
            subprocess.run(
                [
                    "sudo",
                    "-u",
                    "postgres",
                    "psql",
                    "-c",
                    "CREATE DATABASE futbol",
                ]
            )

            # Run database migrations
            subprocess.run(["python3", "manage.py", "makemigrations"])
            subprocess.run(["python3", "manage.py", "migrate"])

            # Create a new superuser
            subprocess.run(
                [
                    "python3",
                    "manage.py",
                    "createsuperuser",
                    f"--username={username}",
                    f"--email={email}",
                    "--noinput",
                ]
            )

            # Set the password for the superuser
            superuser = get_user_model().objects.get(username=f"{username}")
            superuser.set_password(f"{password}")
            superuser.save()

            # Print success message
            self.stdout.write(
                self.style.SUCCESS(
                    "Database reset and superuser created with password."
                )
            )
        except Exception as e:
            # Print error message
            self.stdout.write(self.style.ERROR(f"Error: {str(e)}"))
