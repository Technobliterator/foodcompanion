from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('table/', views.table, name='table'),
	#path('<int:id>', views.product, name='product')
    path('register/', views.register, name='register'),
    path('save-settings/', views.savesettings, name='savesettings'),
    path('', include('django.contrib.auth.urls')),
]