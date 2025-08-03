from django.contrib import admin
from .models import Message, Notification

# Register your models here.
admin.site.register(Message)
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')