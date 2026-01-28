from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


def home(request):
    return render(request, 'accounts/accounts.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect('login')

    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'accounts/login.html')

@login_required
def dashboard(request):
    subscription, created = subscription.objects.get_or_create(
        user=request.user
    )

    return render(request, 'accounts/dashboard.html')

@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'accounts/profile.html', {
        'profile': profile,
    })

def logout_view(request):
    logout(request)
    return redirect('login')
    
