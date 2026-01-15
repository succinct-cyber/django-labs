from django.http import HttpResponse
from django.shortcuts import render

def register_home(request):
    return render(request, 'register/register.html')
# Create your views here.

def register_home(request):
    return render(request, "register/home.html")

def connect_wallet(request):
    return render(request, "register/connect.html")

def profile(request):
    return render(request, "register/profile.html")