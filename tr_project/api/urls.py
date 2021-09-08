from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from .views import TreasureViewSet

router = DefaultRouter()
router.register('treasure', TreasureViewSet, basename='treasure')

urlpatterns = router.urls