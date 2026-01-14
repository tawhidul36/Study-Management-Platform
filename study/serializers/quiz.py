from rest_framework import serializers
from study.models import Quiz, QuizQuestion


class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = [
            'id', 
            'question_text', 
            'option_a', 
            'option_b', 
            'option_c', 
            'option_d', 
            'correct_answer',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']
    
    def validate_correct_answer(self, value):
        if value not in ['A', 'B', 'C', 'D']:
            raise serializers.ValidationError("Correct answer must be A, B, C, or D.")
        return value


class QuizSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    questions = QuizQuestionSerializer(many=True, required=False)
    questions_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Quiz
        fields = [
            'id', 
            'user', 
            'title', 
            'description', 
            'questions',
            'questions_count',
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
    
    def get_questions_count(self, obj):
        return obj.questions.count()
    
    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value
    
    def create(self, validated_data):
        questions_data = validated_data.pop('questions', [])
        quiz = Quiz.objects.create(**validated_data)
        
        for question_data in questions_data:
            QuizQuestion.objects.create(quiz=quiz, **question_data)
        
        return quiz
    
    def update(self, instance, validated_data):
        questions_data = validated_data.pop('questions', None)
        
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        
        if questions_data is not None:
            # Delete existing questions and create new ones
            instance.questions.all().delete()
            for question_data in questions_data:
                QuizQuestion.objects.create(quiz=instance, **question_data)
        
        return instance