from django.urls import path
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.chatPage, name="chat-page"),
    # login-section
    path("auth/login/", LoginView.as_view(template_name="login.html"),
         name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]
