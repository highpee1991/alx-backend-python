from django.db import models
from django.contrib.auth.models import User
from .managers import UnreadMessagesManager


# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited_by =models.BooleanField(default=False)
    read = models.BooleanField(default=False)  # NEW FIELD

    parent_message = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='replies',
        on_delete=models.CASCADE
    )

    objects = models.Manager()  # default manager
    unread = UnreadMessagesManager()  # ✅ custom manager


    def __str__(self):
        return f'from {self.sender} to {self.receiver}: {self.content[:20]}'
    

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    text = models.TextField(default="Notification")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.user}'

    
class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='history')
    old_content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'History for Message ID {self.message.id} at {self.edited_at}'
    
    