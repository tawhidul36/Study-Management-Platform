from rest_framework import serializers
from study.models import Flashcard


class FlashcardSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Flashcard
        fields = ['id', 'user', 'question', 'answer', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
    
    def validate_question(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Question must be at least 3 characters long.")
        return value
    
    def validate_answer(self, value):
        if len(value.strip()) < 1:
            raise serializers.ValidationError("Answer cannot be empty.")
        return value