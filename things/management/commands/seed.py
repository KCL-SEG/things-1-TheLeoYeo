from django.core.management.base import BaseCommand, CommandError
from django.forms import ValidationError
from faker import Faker
import random
from things.models import Bob, Thing


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        self.faker = Faker("en_GB")
        
        
    def handle(self, *args, **options):
        print("Seeding")
        
        for i in range(100):
            thing = Thing(name=self.faker.name(), description=self.faker.text(max_nb_chars=120), quantity=random.randint(0, 100), role=Bob.Greg.value)
            thing.full_clean()
            try:
                thing.full_clean()
                thing.save()
                print("Added user")
            except ValidationError:
                print("Error in adding user.")
            
        
        