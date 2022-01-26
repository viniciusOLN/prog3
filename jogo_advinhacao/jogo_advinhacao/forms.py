from django import forms

class FormGame(forms.Form):
    play = forms.IntegerField(label="jogada", max_value=100)