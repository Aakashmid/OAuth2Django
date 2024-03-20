from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='Home'),
    path('logout/',views.logout_hand,name='Logout user'),
    path('login/',views.login_hand,name='Login user'),
    path('signup/',views.signup_hand,name='Create user'),
    path('accounts/google/login/', views.custom_google_login, name='custom_google_login'),
    path('accounts/github/login/', views.custom_github_login, name='custom_github_login'),
]