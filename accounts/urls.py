from django.urls import path, include
from .views import home, register_wallet, get_wallet_nonce, profile_view
from . import views
from django.contrib.auth.decorators import login_required
from .api_views import test_api
from .api_views import login_api    
from .api_views import ProfileAPIView


urlpatterns = [
    path('', home, name='accounts_home'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/signup/', views.register_view, name='register'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/dashboard/', views.dashboard, name='dashboard'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path("dashboard/", login_required(views.dashboard), name="dashboard"),
    path("api/test/", test_api), 
    path("api/login/", login_api), 
    path('api/profile/', ProfileAPIView.as_view(), name='api-profile'),
    path('api/register-wallet/', views.register_wallet, name='register_wallet'),
    path('api/register-wallet/', register_wallet),
    path('api/wallet-nonce/', get_wallet_nonce),
    path('accounts/payments/', include('payments.urls')),
    path("accounts/billing/", include("payments.urls")),
]

