from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # 로그인 후 홈 페이지로 이동
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'home.html')  # 로그인 페이지로 리턴

def sign_up_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        # Create a new user in the database
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect('login')  # Redirect to login page after successful sign-up
    return render(request, 'sign_up.html')  # Assuming 'sign_up.html' has the sign-up form

def logout_view(request):
    logout(request)
    return redirect('login')