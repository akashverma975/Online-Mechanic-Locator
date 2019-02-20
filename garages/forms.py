from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser


class GarageSignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

    def save(self):
        user = super().save(commit=False)
        user.is_garage = True
        user.save()
        return user
