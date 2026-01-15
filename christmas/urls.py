from django.urls import path
from . import views
from .views import christmas_home

urlpatterns = [
    path('', views.home, name='christmas_home'),
    path("about/", views.about, name="about"),
    path("", christmas_home, name="christmas_home"),
]
