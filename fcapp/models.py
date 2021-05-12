from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    pass

    # add additional fields in here
    country = models.CharField(max_length = 50, default=None, blank=True, null=True)
    store = models.CharField(max_length = 50, default=None, blank=True, null=True)
    glutenfree = models.BooleanField(default=None, blank=True, null=True)
    vegan = models.BooleanField(default=None, blank=True, null=True)
    vegetarian = models.BooleanField(default=None, blank=True, null=True)
    halal = models.BooleanField(default=None, blank=True, null=True)
    kosher = models.BooleanField(default=None, blank=True, null=True)

    def __str__(self):
        return self.username


class FoodProducts(models.Model):
    product = models.TextField(max_length = 255)
    calories = models.IntegerField()
    ingredients = models.TextField(max_length = 500)
    #allergens = models.TextField(max_length = 500)
    country = models.CharField(max_length = 50)
    store = models.CharField(max_length = 50)
    glutenfree = models.BooleanField()
    vegan = models.BooleanField()
    vegetarian = models.BooleanField()
    halal = models.BooleanField()
    kosher = models.BooleanField()

    def __str__(self):
        return self.product