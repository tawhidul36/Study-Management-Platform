from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view/edit it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Check if the object has a user field and it matches the request user
        return obj.user == request.user