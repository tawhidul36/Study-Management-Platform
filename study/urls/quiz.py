from django.urls import path, include
from rest_framework.routers import DefaultRouter
from study.views import QuizViewSet

router = DefaultRouter()
router.register(r'', QuizViewSet, basename='quiz')

urlpatterns = router.urls