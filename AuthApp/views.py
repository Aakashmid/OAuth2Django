from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.models import User

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

def custom_google_login(request):
    # Construct the Google authentication URL
    google_auth_url = "https://accounts.google.com/o/oauth2/v2/auth?client_id=377468363453-8o7g49hofg0lf3oif0gto968vcn3akb6.apps.googleusercontent.com&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Faccounts%2Fgoogle%2Flogin%2Fcallback%2F&scope=email+profile&response_type=code&state=2dq7rIOnrtfnA8Eg&access_type=online"
    
    # Redirect the user to the Google authentication URL
    return redirect(google_auth_url)