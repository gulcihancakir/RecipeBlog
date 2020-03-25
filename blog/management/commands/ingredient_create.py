from django.core.management.base import BaseCommand, CommandError
from blog.models import Ingredient
class Command(BaseCommand):
    def add_arguments(self, parser):
      pass

    def handle(self, *args, **options):
        for i in ['Tomato','Eggplant','Celery','Egg','Milk','Fish','Chicken','Oil' ]:
            Ingredient.objects.create(
                name=i
            )
        print('ingredients add')
