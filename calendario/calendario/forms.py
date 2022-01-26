from calendar import month_name
from django import forms

class FormCalendario(forms.Form):
    month = forms.IntegerField(label="Mês", max_value=31)
    year = forms.IntegerField(label="Ano", )
    