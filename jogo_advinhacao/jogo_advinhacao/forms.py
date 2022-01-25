from django import forms

class FormGame(forms.Form):
    play = forms.IntegerField(label="Tentativa", max_value=100)
        