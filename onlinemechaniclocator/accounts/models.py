from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_mechanic = models.BooleanField(default=False)
    is_garage = models.BooleanField(default=False)

    def __str__(self):
        return self.email
