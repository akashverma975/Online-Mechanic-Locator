from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ['email', 'username', 'is_owner', 'is_mechanic', 'is_garage']


admin.site.register(CustomUser, CustomUserAdmin)
