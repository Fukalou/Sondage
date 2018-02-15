from django import forms
from django.forms import widgets


class LoginForms(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(
        widget= widgets.PasswordInput
    )