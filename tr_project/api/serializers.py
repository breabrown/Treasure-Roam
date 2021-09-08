from rest_framework import serializers
from django.contrib.auth import get_user_model

from tr_app.models import Treasure


class TreasureSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'x_coordinate',
            'y_coordinate',
            'notes',
            'placed_by',
            'date_created',
            'last_visit',
        )
        model = Treasure