# _*_ coding: utf-8 _*_
from django.contrib.auth.models import Group
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from projekty.models import Student, Przedmiot, Projekt, Prowadzacy, Wybrany_projekt
import datetime
from django.http import HttpResponse

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


@csrf_exempt
def your_data(request):
    now = datetime.datetime.now()
    projects_id = Wybrany_projekt.objects.filter(id_student=request.user.username, akceptacja="True")
    projects_id2 = Wybrany_projekt.objects.filter(id_student=request.user.username, akceptacja='')

    if request.method == 'POST':
        request.user.email = request.POST['email']
        request.user.save()


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
        'projects': projects_id,
        'projects2': projects_id2,
    }
    return render(request, 'your_data.html', context)


@csrf_exempt
def projects(request):
    global z
    if request.user.is_authenticated():
        username = request.user.username
    else:
        username = None
    tok = Student.objects.filter(id_student=username).values('tok_studiow')
    name = Projekt.objects.values('id_projektu')
    for i in tok:
        z = i['tok_studiow']

    lessons2 = Przedmiot.objects.raw('SELECT DISTINCT projekty_projekt.*,projekty_przedmiot.*, '
                                     'projekty_przedmiot.nazwa AS name FROM projekty_projekt INNER JOIN projekty_przedmiot '
                                     'ON projekty_przedmiot.id_przedmiotu=projekty_projekt.id_przedmiotu_id '
                                     'WHERE projekty_przedmiot.tok_studiow = %s ', [z])

    if request.method == 'POST':
        Wybrany_projekt.objects.create(id_projektu=Projekt.objects.get(id_projektu=request.POST['succes2']),
        id_student=Student.objects.get(id_student=username),
        preferencja=request.POST['succes4'],licznosc_grupy=request.POST['succes3'])


    name = Przedmiot.objects.raw(
        'SELECT DISTINCT projekty_przedmiot.* FROM projekty_przedmiot WHERE tok_studiow = %s', [z])
    context = {
        'lessons': lessons2,
        'name':name,
    }
    return render(request, 'projects.html', context)






