# # chats/views.py

# from django.views.decorators.cache import cache_page
# from django.shortcuts import render
# from messaging.models import Message
# from django.contrib.auth.decorators import login_required

# @cache_page(60)  # Cache for 60 seconds
# @login_required
# def inbox_view(request):
#     messages = Message.objects.filter(receiver=request.user)
#     return render(request, 'inbox.html', {'messages': messages})
