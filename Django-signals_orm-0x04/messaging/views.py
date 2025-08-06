from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


# Create your views here.
@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return redirect('home') #wherever you want to redirect after deleting
    


@login_required
def home(request):
    return render(request, 'home.html')