from django.contrib import admin

# Register your models here.
from .models import *


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id_prowadzacego','nazwisko', 'imie', 'tytul','stanowisko')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id_student', 'nazwisko', 'imie','tok_studiow')


class PrzedmiotAdmin(admin.ModelAdmin):
    list_display = ('id_przedmiotu','nazwa', 'id_prowadzacego', 'typ_zajec','tok_studiow')


class ProjektAdmin(admin.ModelAdmin):
    list_display = ('id_projektu','nazwa', 'id_przedmiotu', 'liczba_miejsc')


class WybranypAdmin(admin.ModelAdmin):
    list_display = ('id_projektu', 'id_student', 'akceptacja')


admin.site.register(Prowadzacy,TeacherAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Projekt,ProjektAdmin)
admin.site.register(Przedmiot,PrzedmiotAdmin)
admin.site.register(Wybrany_projekt,WybranypAdmin)