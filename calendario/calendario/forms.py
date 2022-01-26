from calendar import month_name
from django import forms

class FormCalendario(forms.Form):
    month = forms.IntegerField(label="Mês", min_value=1, max_value=12)
    year = forms.IntegerField(label="Ano")
    