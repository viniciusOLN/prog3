from django import forms

class FormGame(forms.Form):
    play = forms.IntegerField(max_value=100, widget=forms.TextInput(attrs={'placeholder': 'Jogada'}))
