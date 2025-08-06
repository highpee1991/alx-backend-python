"""
URL configuration for DjangoSignalsProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from messaging.views import delete_user, conversation_page
from django.views.generic import TemplateView
from messaging.views import unread_messages_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('delete_user/', delete_user, name='delete_user'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('threaded/', conversation_page, name='threaded_conversations'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('inbox/unread/', unread_messages_view, name='unread_messages'),
]
