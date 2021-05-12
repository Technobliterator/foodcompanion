# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import RegisterForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', ]

admin.site.register(CustomUser, CustomUserAdmin)