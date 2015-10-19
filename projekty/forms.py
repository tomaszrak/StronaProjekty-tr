# _*_ coding: utf-8 _*_

from django import forms
from .models import *


class Login(forms.Form):
    username = forms.CharField(label="Login(numer indeksu):",max_length=30)
    password = forms.CharField(label="Hasło:",widget=forms.PasswordInput())





