from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from things.models import Thing


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')
        
        
    def handle(self, *args, **options):
        print("Lool")
        Thing.objects.filter(id__gte=6).delete()
