from django.urls import path, include
from .views import home, user_profile
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    
    path('login/', views.login_view, name='login'),
    path('signup/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('accounts/payments/', include('subscriptions_access.urls')),
    path("accounts/billing/", include("subscriptions_access.urls")),
    path('api/profile/', user_profile),
]

