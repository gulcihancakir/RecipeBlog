from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


ingredient_choices = (('Tomato', 'Tomato'),
                          ('Eggplant', 'Eggplant'),
                          ('Celery', 'Celery'),
                          ('Egg', 'Egg'),
                          ('Milk', 'Milk'),
                          ('Fish', 'Fish'),
                          ('Chicken', 'Chicken'),
                          ('Oil', 'Oil')
                          )

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    difficulty_choices = (
        ('easy', 'easy'),
        ('medium', 'medium'),
        ('hard', 'hard')
    )
    level = models.CharField(max_length=6, choices=difficulty_choices)
    
    ingredients = MultiSelectField(choices=ingredient_choices)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.recipe_name
