from rest_framework import serializers
from study.models import MatchingItem


class MatchingItemSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = MatchingItem
        fields = ['id', 'user', 'term', 'definition', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
    
    def validate_term(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Term must be at least 2 characters long.")
        return value
    
    def validate_definition(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Definition must be at least 3 characters long.")
        return value