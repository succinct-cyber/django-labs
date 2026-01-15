from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Subscription(models.Model):
    PLAN_CHOICES = (
        ('free', 'Free'),
        ('pro', 'Pro'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="subscription"
    )
    plan = models.CharField(max_length=50, default='free')
    is_active = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} – {self.plan}"

