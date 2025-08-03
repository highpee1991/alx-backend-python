from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to allow only participants of a conversation to access messages and conversations.
    """

    def has_object_permission(self, request, view, obj):
        # Allow only authenticated users
        if not request.user or not request.user.is_authenticated:
            return False

        # Check for safe methods like GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            if hasattr(obj, 'participants'):
                return request.user in obj.participants.all()
            if hasattr(obj, 'conversation'):
                return request.user in obj.conversation.participants.all()
        else:
            # For PUT, PATCH, DELETE – check if the user is a participant
            if hasattr(obj, 'participants'):
                return request.user in obj.participants.all()
            if hasattr(obj, 'conversation'):
                return request.user in obj.conversation.participants.all()

        return False
