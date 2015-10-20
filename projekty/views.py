from django.shortcuts import render
from .forms import Login

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    return render(request, 'contact.html', {})
