from rest_framework import generics, serializers, viewsets
from tr_app.models import Treasure
from .serializers import TreasureSerializer

class TreasureViewSet(viewsets.ModelViewSet):
    queryset = Treasure.objects.all()
    serializer_class = TreasureSerializer