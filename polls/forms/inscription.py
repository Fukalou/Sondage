from django import forms
from django.forms import widgets


class InscriptionForms(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(
        widget= widgets.PasswordInput
    )
    password_confirm = forms.CharField(
        widget= widgets.PasswordInput
    )