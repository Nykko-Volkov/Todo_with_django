from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TodoItem
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


@login_required  # Ensure that the user is logged in to access this view
def index(request):
    todo_items = TodoItem.objects.filter(user=request.user)  # Filter todo items by the logged-in user
    return render(request, 'todo_app/index.html', {'todos': todo_items})  # Render the index template with the todo items


def login_function(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    return render(request, 'todo_app/signin.html')  # Render the login template

def signup_function(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')  # Redirect to login after signup
    return render(request, 'todo_app/signup.html')  # Render the signup template


def logout_function(request):
    if request.method == 'POST':
        logout(request)  # Log out the user
        return redirect('login')  # Redirect to login after logout
    return render(request, 'todo_app/logout.html')  # Render the logout template