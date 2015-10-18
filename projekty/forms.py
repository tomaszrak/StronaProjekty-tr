# _*_ coding: utf-8 _*_

from django import forms
from .models import *

class Login(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id_student','tok_studiow']




