# -*- coding: utf-8 -*-

from django.db import models
from registration.signals import user_registered


# Create your models here.


class Student(models.Model):
    id_student = models.CharField('Numer indeksu', max_length=30, primary_key=True)
    nazwisko = models.CharField('Nazwisko', max_length=30)
    imie = models.CharField('Imię', max_length=30)
    tok_studiow = models.CharField('Tok studiów', max_length=30)

    class Meta:
        verbose_name_plural = "Student"

    def __unicode__(self):  # wyświetla nazwisko i imie w panelu administratora
        return u'%s %s' % (self.nazwisko, self.imie)


class Prowadzacy(models.Model):
    id_prowadzacego = models.CharField('ID prowadzacego', max_length=30, primary_key=True)
    nazwisko = models.CharField('Nazwisko', max_length=30)
    imie = models.CharField("Imię", max_length=30)
    tytul = models.CharField("Tytuł", max_length=30)
    stanowisko = models.CharField('Stanowisko', max_length=30)

    class Meta:
        verbose_name_plural = "Prowadzący"

    def __unicode__(self):
        return u'%s %s' % (self.nazwisko, self.imie)


class Przedmiot(models.Model):
    id_przedmiotu = models.CharField('ID przedmiotu', max_length=30, primary_key=True)
    nazwa = models.CharField('Nazwa przedmiotu', max_length=50)
    tok_studiow = models.CharField('Tok studiów', max_length=30)
    grupa = models.CharField('Grupa', max_length=30)
    id_prowadzacego = models.ForeignKey(Prowadzacy)
    typ_zajec = models.CharField('Typ zajęć', max_length=50)

    class Meta:
        verbose_name_plural = "Przedmiot"  # dzieki temu python nie wypisuje nazwy z końcówką "s" jako lb mnoga

    def __unicode__(self):
        return u'%s' % (self.nazwa)


class Projekt(models.Model):
    id_projektu = models.CharField('ID projektu', max_length=30, primary_key=True)
    id_przedmiotu = models.ForeignKey(Przedmiot)
    nazwa = models.CharField('Nazwa projektu', max_length=50)
    liczba_miejsc = models.IntegerField('Lb. miejsc')

    class Meta:
        verbose_name_plural = "Projekt"

    def __unicode__(self):
        return u'%s' % (self.nazwa)


class Wybrany_projekt(models.Model):
    id_projektu = models.ForeignKey(Projekt)
    id_student = models.ForeignKey(Student)
    akceptacja = models.BooleanField('Akceptacja', default=False)
    preferencja = models.CharField('Preferencja', max_length=30)
    komentarz = models.CharField('Komentarz', max_length=100, blank=True)
    licznosc_grupy = models.IntegerField('Liczność grupy')

    class Meta:
        verbose_name_plural = "Wybrany projekt"

    def __unicode__(self):
        return u'%s %s' % (self.id_student, self.id_projektu)


def user_registered_callback(sender, user, request, **kwargs):
    profile = Student(id_student=user)
    profile.nazwisko = (request.POST["last_name"])
    profile.imie = (request.POST["first_name"])
    profile.tok_studiow = (request.POST["tok_studiow"])
    profile.save()


user_registered.connect(user_registered_callback)
