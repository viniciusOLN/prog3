from django import forms

class FormFile(forms.Form):
    tsv_file = forms.FileField()
    checkbox = forms.BooleanField(label="Remover todos os registros?")

class FormSearch(forms.Form):
    search = forms.NumberInput()