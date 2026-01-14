from django.urls import path, include
from rest_framework.routers import DefaultRouter
from study.views import FlashcardViewSet

router = DefaultRouter()
router.register(r'', FlashcardViewSet, basename='flashcard')

urlpatterns = router.urls