from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Ingredient(models.Model):
    name = models.CharField(max_length=255,unique=True)
    posts = models.ManyToManyField('Post', null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    likes = models.ManyToManyField(User,related_name="likes",blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    ingredients = models.ManyToManyField('Ingredient', null=True, blank=True)
    difficulty_choices = (
        ('easy', 'easy'),
        ('medium', 'medium'),
        ('hard', 'hard')
    )
    INTEGER_CHOICES= [tuple([x,x]) for x in range(1,6)]
    level = models.CharField(max_length=6, choices=difficulty_choices,null=True,blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.recipe_name

    def get_absolute_url(self):
        return reverse("recipe_detail",args=[self.pk])
