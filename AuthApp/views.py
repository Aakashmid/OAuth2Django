from django.shortcuts import render
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from .models import MyForm
# Create your views here.
def home(request):
    Users=User.objects.all()
    return render(request,'AuthApp/index.html',{"Users":Users})
def login_hand(request):
    return render(request,'AuthApp/login.html')
def logout_hand(request):
    logout(request)
    return render(request,'AuthApp/index.html')
def signup_hand(request):
    return render(request,'AuthApp/signup.html')