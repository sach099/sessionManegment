from django import forms

class Name(forms.Form):
    username = forms.CharField()

class Age(forms.Form):
    userage = forms.IntegerField()

class Gf(forms.Form):
    gf_name = forms.CharField()