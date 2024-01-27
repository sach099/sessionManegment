from django import forms

class Login(forms.Form):
    name = forms.CharField()