from django.urls import path
from .views import register_home
from django.urls import path
from . import views

urlpatterns = [
    path('', register_home, name='register_home'),

]

urlpatterns = [
    path("", views.register_home, name="register_home"),
    path("connect/", views.connect_wallet, name="connect_wallet"),
    path("profile/", views.profile, name="profile"),
]
