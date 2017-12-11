from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    """Custom permission class to allow only bucketlist owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the bucketlist owner."""
        return obj == request.user
