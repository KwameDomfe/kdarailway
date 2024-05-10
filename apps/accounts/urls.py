from django.urls import path
from .views import (accounts_layout,login_view, logout_view, register_view)

app_name = 'accounts'

urlpatterns = [
    # Accounts
    path("accounts_layout/", accounts_layout, name="accounts-layout"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
]
