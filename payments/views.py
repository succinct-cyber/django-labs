from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils import timezone
from datetime import timedelta

@login_required
def activate_pro(request):
    sub = request.user.subscription
    sub.plan = 'pro'
    sub.is_active = True
    sub.expires_at = timezone.now() + timedelta(days=30)
    sub.save()

    return redirect('profile')


# Create your views here.
