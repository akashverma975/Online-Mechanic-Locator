from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser


class MechanicSignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

    def save(self):
        user = super().save(commit=False)
        user.is_mechanic = True
        user.save()
        return user
