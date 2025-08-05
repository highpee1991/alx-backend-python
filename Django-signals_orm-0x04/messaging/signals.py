from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Notification, Message, MessageHistory

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    print("🚨 Signal Fired: create_notification")
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)


@receiver(pre_save, sender=Message)
def log_message_edites(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Message.objects.get(pk=instance.pk)
        except Message.DoesNotExist:
            return
        
        if old_instance.content != instance.content:
            instance.edited = True

            #log the old contents
            MessageHistory.objects.create(
                message = instance,
                old_content = old_instance.content
            )