from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.core import serializers
from .models import FoodProducts
from .filters import FoodProductsFilter
from .forms import CustomUserChangeForm, RegisterForm
import json

# Create your views here.

def index(response):
	'''
	products = FoodProducts.objects.all()
	filter = FoodProductsFilter(response.GET, queryset=products)
	products = filter.qs
	'''

	return render(response, 'home.html')

def table(response):
	products = FoodProducts.objects.order_by('product')
	
	filter = FoodProductsFilter(response.GET, queryset=products)

	#vegetarian = FoodCompanion.objects.filter(Q(vagan__iexact = 'True') | Q(vegetarian__iexact = 'True'))

	raw_data = serializers.serialize('python', filter.qs)
	actual_data = [d['fields'] for d in raw_data]
	json_products = json.dumps(actual_data)

	return HttpResponse(json_products, content_type="application/json")

def register(response):
	if response.method == 'POST':
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = RegisterForm()

	return render(response, 'registration/register.html', {'form': form})

def savesettings(response):
    if response.method == 'POST' and response.user.is_authenticated:
        u_form = CustomUserChangeForm(response.POST,instance=response.user)
        if u_form.is_valid():
	        u_form.save()
        return ''
    else:
        return redirect('index')

'''
def product(response, id):
	item = FoodProducts.objects.get(id=id)
	return render(response, 'product.html', { 'title': item.product, 'item': item })
'''
