from django.db import models
from django.conf import settings


class Flashcard(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='flashcards'
    )
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Flashcard'
        verbose_name_plural = 'Flashcards'
    
    def __str__(self):
        return f"{self.user.email} - {self.question[:50]}"