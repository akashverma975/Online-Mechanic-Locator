from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email
