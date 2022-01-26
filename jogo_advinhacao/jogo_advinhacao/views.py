from django.shortcuts import render
from jogo_advinhacao.forms import FormGame
import random

def newNum():   
    return int(random.sample([i for i in range(100)], 1)[0])

NUM = int(newNum())

def play_game(request, chances): 
    print(NUM) 
    form = FormGame(request.POST)
    value = int(form['play'].value())
    fim = None
    ganhar = None
    msg = None

    if(chances == 0):
        fim = "Que pena! Acabaram as tentativas! O número era: " + str(NUM)
    
    if(value > NUM ):
        msg = "MENOR QUE "
        chances = chances - 1
    elif (value < NUM ):
        msg = "MAIOR QUE "
        chances = chances - 1
    else:
        ganhar = "Parabéns! Você ganhou!"


    context = {
        'form': form,        
        'chances': chances,
        'msg': msg,
        'fim': fim,
        'value': value,
        'ganhar': ganhar,
    }
    return render(request, 'index.html', context=context)