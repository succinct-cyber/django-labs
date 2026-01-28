from django.http import HttpResponse
from django.shortcuts import render

def register_home(request):
    return render(request, 'webhooks_signals/register.html')
# Create your views here.

def register_home(request):
    return render(request, "webhooks_signals/home.html")

def connect_wallet(request):
    return render(request, "webhooks_signals/connect.html")

def profile(request):
    return render(request, "webhooks_signals/profile.html")