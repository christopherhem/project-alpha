from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

# from accounts.views import register


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # path("signup/", register, name="signup"),
]
