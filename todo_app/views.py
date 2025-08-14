
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TodoItem
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


@login_required
def index(request):
    todo_items = TodoItem.objects.filter(user=request.user)
    return render(request, 'todo_app/index.html', {'todos': todo_items})
@login_required
def save_todo(request):
    if request.method == 'POST':
        title = request.POST.get('inputfromhtml')
        if title:
            TodoItem.objects.create(user=request.user, title=title)
            messages.success(request, 'Todo added!')
        else:
            messages.error(request, 'Todo cannot be empty.')
    return redirect('index')

@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id, user=request.user)
    todo.delete()
    messages.success(request, 'Todo deleted!')
    return redirect('index')


def login_function(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'todo_app/signin.html')

def signup_function(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Account created! Please sign in.')
            return redirect('signin')
    return render(request, 'todo_app/signup.html')


def logout_function(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('signin')
