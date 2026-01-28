from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.user.username

# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_payment_intent = models.CharField(max_length=255)
    amount = models.IntegerField()  # cents
    currency = models.CharField(max_length=10, default='usd')
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"
    

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tx_hash = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.tx_hash}"
    
    from django.db import models
from django.contrib.auth.models import User

class Wallet_connect(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet_address = models.CharField(
        max_length=42,
        blank=True,
        null=True,
        unique=True
    )

    def __str__(self):
        return f"{self.user.username} Wallet_connect"
