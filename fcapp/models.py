from django.db import models

# Create your models here.

class FoodProducts(models.Model):
    product = models.TextField(max_length = 255)
    calories = models.IntegerField()
    ingredients = models.TextField(max_length = 500)
    allergens = models.TextField(max_length = 500)
    country = models.CharField(max_length = 50)
    store = models.CharField(max_length = 50)
    glutenfree = models.BooleanField()
    vegan = models.BooleanField()
    vegetarian = models.BooleanField()
    halal = models.BooleanField()
    kosher = models.BooleanField()

from models import FoodProducts
from django.db.models import Q

# 1. query all items form foodproducts where country = 'United States'
country = FoodProducts.objects.filter(country__iexact = 'United States')
print(country)
# 2. all the ones from Wholefood
store = FoodProducts.objects.filter(store__iexact = 'Wholefoods')
print(store)
# 3. all the ones with less than 300 calories
calories = FoodProducts.objects.filter(calories__lt < 300)
print(calories)
# 4. all the ones listed as Vegan
vegan = FoodProducts.objects.filter(vagan__iexact = 'True')
print(vegan)
# 5. all the ones Vegetarian
vegetarian = FoodProducts.objects.filter(Q(vagan__iexact = 'True') | Q(vegetarian__iexact = 'True'))
