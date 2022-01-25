from django.shortcuts import render
from jogo_advinhacao.forms import FormGame
import random

def newNum():   
    return random.sample([i for i in range(100)], 1)

CHANCES = 5
NUM = newNum()

def index(request):
    form = FormGame(request.GET or None)
    if form.is_valid():
        num = NUM        
        if form['play'] > num:
            text = 'maior que ' + form['play']            
        elif form['play'] < num:
            text = 'menor que ' + form['play']
        else:
            text='Parabéns! Você acertou!'

    return render(request, 'index.html', locals())