from rest_framework import serializers
from .models import User, Message, Conversation
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ['user_id', 'email', 'phone_number', 'role', 'password', 'created_at']

        def validate_email(self, value):
            if not value.endswith('@example.com'):
                raise ValidationError("Only @example.com emails are allowed.")
            return value
    

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    class Meta:
        model = Message
        feilds = ['message_id', 'sender', 'conversation', 'message_body', 'sent_at']


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = serializers.SerializerMethodField()
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at']

    def get_messages(self, obj):
        messages = obj.messages.all()
        return MessageSerializer(messages, many=True).data


