import json

from rest_framework.permissions import BasePermission

from users.models import User
from users.serializers import UserUpdateSerializer, UserSerializer


class AdUpdateDeletePermission(BasePermission):
    message = "Permission Denied"

    def has_object_permission(self, request, view, obj):
        user = User.objects.get(username=request.user.username)

        if user.role == 'admin' or 'moderator':
            return True
        elif user.id == obj.author_id:
            return True
        else:
            return False
