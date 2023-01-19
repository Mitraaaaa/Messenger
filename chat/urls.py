from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.chatPage, name="index"),
    path('account/<str:username>/', views.account, name='acc'),
    path('account/<str:username>/delete/', views.deleteAcc, name='del'),
    path('account/<str:username>/edit-first-name/<str:new_fname>/', views.editFirstName, name='new-fname'),
    path('account/<str:username>/edit-last-name/<str:new_lname>/', views.editLastName, name='new-lname'),
    path('account/<str:username>/edit-username/<str:new_username>/', views.editUsername, name='new-user'),
    path('account/<str:username>/edit-email/<str:new_email>/', views.editEmail, name='new-email'),
    path('<str:room_name>/', views.room, name='room'),

    # login-section
    path("auth/login/", LoginView.as_view(template_name="login.html"),
         name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]
