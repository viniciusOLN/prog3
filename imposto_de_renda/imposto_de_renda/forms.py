from django import forms

class FormRenda(forms.Form):
    name = forms.CharField(label="Nome", max_length=100)
    annual_income = forms.FloatField(label="Renda Anual", min_value= 0.00)
    dependents = forms.IntegerField(label="Dependentes", min_value= 0)