from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from study.models import Quiz
from study.serializers import QuizSerializer
from study.permissions import IsOwner


class QuizViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Quizzes
    Provides: list, create, retrieve, update, partial_update, destroy
    """
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        # Users can only see their own quizzes
        return Quiz.objects.filter(user=self.request.user).prefetch_related('questions')
    
    def perform_create(self, serializer):
        # Automatically assign the current user
        serializer.save(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'message': 'Quiz created successfully',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'message': 'Quiz updated successfully',
            'data': serializer.data
        })
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {'message': 'Quiz deleted successfully'},
            status=status.HTTP_200_OK
        )