from django.shortcuts import render
from .models import MyForm
# Create your views here.
def home(request):
    form=MyForm()
    return render(request,'AuthApp/index.html',{'form':form})