from django.shortcuts import render
from .forms import Login

# Create your views here.


def home(request):
    form = Login()
    context = {
        "form": form,
    }
    if request.method == "POST":
        context = {
            "form": form,
        }
    return render(request, 'home.html', context)


def contact(request):
    return render(request, 'contact.html', {})
