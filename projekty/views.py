from django.shortcuts import render
from .forms import Login

# Create your views here.


def home(request):
    title = "Siemano %s" % request.user
    form = Login()
    context = {
        "template": title,
        "form": form,
    }

    if request.method == "POST":
        context = {
            "template": "Thank you",
            "form": form,
        }
    return render(request, 'home.html', context)
