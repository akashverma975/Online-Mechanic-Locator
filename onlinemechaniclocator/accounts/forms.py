from django.contrib.auth.forms import UserCreationForm
from .models import User


class OwnerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_owner = True
        user.save()
        return user


class MechanicSignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_mechanic = True
        user.save()
        return user


class GarageSignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_garage = True
        user.save()
        return user
