from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

def home(request):
    return render(request, 'accounts/accounts.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        return redirect('login')

    return render(request, 'accounts/register.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(
                request,
                'accounts/login.html',
                {'error': 'Invalid username or password'}
            )

    return render(request, 'accounts/login.html')


def dashboard(request):
    return HttpResponse(
        f"""
        Authenticated: {request.user.is_authenticated}<br>
        User: {request.user}<br>
        Session key: {request.session.session_key}
        """
    )

    subscription = None

    return render(request, 'accounts/dashboard.html', {'subscription': subscription
    })

@login_required(login_url="login")
def profile_view(request):
    profile = request.user.profile
    return render(request, 'accounts/profile.html', {
        'profile': profile,
    })


def logout_view(request):
    logout(request)
    return redirect('login')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    return Response({
        "username": user.username,
        "email": user.email,
    })
    