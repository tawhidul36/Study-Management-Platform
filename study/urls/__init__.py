from django.urls import path, include

urlpatterns = [
    path('flashcards/', include('study.urls.flashcard')),
    path('quizzes/', include('study.urls.quiz')),
    path('matching-items/', include('study.urls.matching_item')),
    path('notes/', include('study.urls.note')),
]