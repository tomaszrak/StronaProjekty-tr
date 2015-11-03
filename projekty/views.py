# _*_ coding: utf-8 _*_
from django.contrib.auth.models import Group
from django.shortcuts import render
#from .forms import Login,Registration
from projekty.models import Student
from projekty.forms import Registration
import datetime
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.


def home(request):
   # k = []
   # for item in Student.objects.all():
   #     k.append(item.id_student)

   # context = {
   #        'data': k
   #     }
   group = Group.objects.get(name="Nauczyciele")
   if group in request.user.groups.all():
       ss = True
   else:
       ss = False
   context = {
       'group': ss,
   }
   return render(request, 'home.html', context)


def contact(request):
    return render(request, 'contact.html', {})


def your_data(request):
    now = datetime.datetime.now()
    if request.user.is_authenticated():
        username = request.user.username
        name = Student.objects.get(id_student=username)
        email = request.user.email
    else:
        name = "Jesteś nie zalogowany"
        email = "none"
    context = {
       'email':email,
        'now': now,
       'name': name,
    }
    return render(request, 'your_data.html', context)


def projects(request):
    if request.user.is_authenticated():
        name = True
    else:
        name = False
#    form = Registration(request.POST or None)
    context = {
       'name': name,
    }
    return render(request, 'projects.html', context)





