# _*_ coding: utf-8 _*_
from django.contrib.auth.models import Group
from django.shortcuts import render
from projekty.models import Student, Przedmiot, Projekt, Prowadzacy
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
        'email': email,
        'now': now,
        'name': name,
    }
    return render(request, 'your_data.html', context)


def projects(request):
    global z
    if request.user.is_authenticated():
        username = request.user.username
    else:
        username = None
    tok = Student.objects.filter(id_student=username).values('tok_studiow')
    for i in tok:
        z = i['tok_studiow']

    # object = Przedmiot.objects.filter(tok_studiow=tok).values('id_przedmiotu')
    lessons2 = Przedmiot.objects.raw('SELECT DISTINCT projekty_projekt.*,projekty_przedmiot.*, '
            'projekty_przedmiot.nazwa AS name FROM projekty_projekt INNER JOIN projekty_przedmiot '
            'ON projekty_przedmiot.id_przedmiotu=projekty_projekt.id_przedmiotu_id '
                                     'WHERE projekty_przedmiot.tok_studiow = %s ',[z])
    context = {
        'lessons': lessons2,
    }
    return render(request, 'projects.html', context)
