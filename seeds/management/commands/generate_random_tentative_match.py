from django.core.management.base import BaseCommand
from seeds.scripts.matches import generate_random_tentative_match


class Command(BaseCommand):
    def handle(self, *args, **options):
        generate_random_tentative_match(self)
