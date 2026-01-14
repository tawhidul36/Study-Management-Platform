from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Flashcard, Quiz, QuizQuestion, MatchingItem, Note


@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'question', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['question', 'answer', 'user__email']
    readonly_fields = ['created_at', 'updated_at']


class QuizQuestionInline(admin.TabularInline):
    model = QuizQuestion
    extra = 1


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['title', 'description', 'user__email']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [QuizQuestionInline]


@admin.register(MatchingItem)
class MatchingItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'term', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['term', 'definition', 'user__email']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['title', 'content', 'user__email']
    readonly_fields = ['created_at', 'updated_at']