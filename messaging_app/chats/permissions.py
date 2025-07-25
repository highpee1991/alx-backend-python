from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to view or edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return hasattr(obj, 'user') and obj.user == request.user

    
class IsParticipantOfConversation(BasePermission):
    """
    Only allows participants of a conversation to view/edit messages or the conversation itself.
    """
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'conversation'):
            # Object is a Message
            return request.user in obj.conversation.participants.all()
        elif hasattr(obj, 'participants'):
            # Object is a Conversation
            return request.user in obj.participants.all()
        return False