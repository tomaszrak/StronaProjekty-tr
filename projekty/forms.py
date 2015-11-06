# _*_ coding: utf-8 _*_
from registration.forms import RegistrationForm
from django import forms
from .models import *



class Login(forms.Form):
    username = forms.CharField(label="Login(numer indeksu):",max_length=30)
    password = forms.CharField(label="Hasło:",widget=forms.PasswordInput())


class Registration(RegistrationForm):
    username = forms.CharField(label="Login(numer indeksu):",max_length=30)
    first_name = forms.CharField(label="Imię:")
    last_name = forms.CharField(label="Nazwisko:")
    email = forms.EmailField(label="Email:")
    tok_studiow = forms.CharField(label="Tok Studiów:")
    password1 = forms.CharField(label="Hasło:",widget=forms.PasswordInput())
    password2 = forms.CharField(label="Powtórz hasło:",widget=forms.PasswordInput())







