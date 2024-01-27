from django import forms

class Name(forms.Form):
    name = forms.CharField()

class Age(forms.Form):
    age = forms.IntegerField()

class Gf(forms.Form):
    gf_name = forms.CharField()