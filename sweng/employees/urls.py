from django.urls import path, include
from . import views
from .views import home

urlpatterns = [
    path('', home, name='employees_home'),
    path('<int:employee_id>/', views.employee_detail, name='employee_detail'),
]
