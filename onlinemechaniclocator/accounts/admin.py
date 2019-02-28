from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ['email', 'username', 'is_owner', 'is_mechanic', 'is_garage']


admin.site.register(User, CustomUserAdmin)
