from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField

class CustomUser(AbstractUser):
    # visited, this is where i would put the attribute to store all geocaches a user has visited
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)

    def __str__(self):
        return self.username