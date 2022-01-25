from django.shortcuts import render
from jogo_advinhacao.forms import FormGame
import random

def play_game(request,numero_sorteado, chances):
    form = FormGame(request.POST)
    value = int(form['play'].value())
    fim = None

    if(chances == 0):
        fim = "Que pena! acabaram as tentativas! você perdeu o jogo"
    
    if(value > numero_sorteado ):
        msg = "menor que "+ str(value)
        chances = chances - 1
    elif (value < numero_sorteado):
        msg = "maior que" + str(value)
        chances = chances - 1
    else:
        msg = "Parabens! voce ganhou"

    context = {
        'form': form,
        'numero_sorteado': numero_sorteado,
        'chances': chances,
        'msg': msg,
        'fim': fim
    }
    return render(request, 'index.html', context=context)

def index(request):
    if request.method == "POST":
        pass
    else:
        form = FormGame()
        chances = 5
        list_values = [i for i in range(100)]
        numero_sorteado = random.sample(list_values, 1)
        print(numero_sorteado, chances)
        context = {
            'form': form,
            'numero_sorteado': numero_sorteado[0],
            'chances': chances
        }

    return render(request, 'index.html', context=context)