from django import forms

class Additems(forms.Form):
    itemname = forms.CharField()
    quantity = forms.IntegerField()