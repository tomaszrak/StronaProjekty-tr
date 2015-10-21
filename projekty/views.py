from django.shortcuts import render
from .forms import Login,Registration

# Create your views here.


def home(request):
    form = Registration(request.POST or None)
    context = {
       'form': form,
    }
    return render(request, 'home.html', context)


def contact(request):
    return render(request, 'contact.html', {})




