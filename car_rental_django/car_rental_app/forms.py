from django import forms
from django.forms import ModelForm
from .models import *

class register_form(ModelForm):
    class Meta:
        model=credentials
        fields="__all__"
        widgets={"password":forms.PasswordInput()}

class login_form(ModelForm):
    class Meta:
        model=credentials
        fields=("name","password")
        widgets={"password":forms.PasswordInput()}