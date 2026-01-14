from django.urls import path, include
from rest_framework.routers import DefaultRouter
from study.views import MatchingItemViewSet

router = DefaultRouter()
router.register(r'', MatchingItemViewSet, basename='matching-item')

urlpatterns = router.urls