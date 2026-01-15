from django.urls import path
from . import views

urlpatterns = [
    path('activate/', views.activate_pro, name='activate_pro'),
]
