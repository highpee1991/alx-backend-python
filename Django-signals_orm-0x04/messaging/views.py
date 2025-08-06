from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Message
from django.http import JsonResponse
from django.db.models import Q


# Create your views here.
@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return redirect('home') #wherever you want to redirect after deleting
    


@login_required
def home(request):
    return render(request, 'home.html')

messages = Message.objects.filter(parent_message__isnull=True).select_related('sender').prefetch_related('replies__sender')

def get_threaded_messages(message):
    """
    Recursively gets message and its nested replies
    """
    threaded = {
        'id': message.id,
        'sender': message.sender.username,
        'content': message.content,
        'timestamp': message.timestamp,
        'replies': []
    }

    for reply in message.replies.all():
        threaded['replies'].append(get_threaded_messages(reply))
    
    return threaded


def conversation_view(request):
    user = request.user
    top_level_messages = Message.objects.filter(
        sender=user,
        parent_message__isnull=True
    ).select_related('sender').prefetch_related('replies__sender')

    threaded_conversations = [get_threaded_messages(msg) for msg in top_level_messages]

    return JsonResponse({'conversations': threaded_conversations})


@login_required
def conversation_page(request):
    user = request.user
    messages = Message.objects.filter(
        Q(sender=user) | Q(receiver=user),
        parent_message__isnull=True
    ).select_related('sender').prefetch_related('replies__sender')

    return render(request, 'threaded_messages.html', {'messages': messages, 'level': 0})

