import datetime
from django.db import models
from django.contrib.auth import get_user_model

from tr_app.models import Treasure

class Treasure(models.Model):
    x_coordinate = models.FloatField()
    y_coordinate = models.FloatField()
    notes = models.TextField()
    placed_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateTimeField(auto_now_add=True)