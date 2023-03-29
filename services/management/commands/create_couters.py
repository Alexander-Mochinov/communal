from django.core.management.base import BaseCommand, CommandError
from services.models import Counter


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        ...

    def handle(self, *args, **options):
        for counter in Counter.Parameter:
            _ = Counter.objects.create(name=counter)
