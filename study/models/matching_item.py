from django.db import models
from django.conf import settings


class MatchingItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='matching_items'
    )
    term = models.CharField(max_length=255)
    definition = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Matching Item'
        verbose_name_plural = 'Matching Items'
    
    def __str__(self):
        return f"{self.user.email} - {self.term}"