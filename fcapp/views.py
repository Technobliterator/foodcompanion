from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodProducts

# Create your views here.

def index(response):
	products = FoodProducts.objects.all()
	return render(response, 'home.html', { 'products': products })

def product(response, id):
	item = FoodProducts.objects.get(id=id)
	return render(response, 'product.html', { 'title': item.product, 'item': item })