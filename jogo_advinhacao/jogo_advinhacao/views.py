from django.shortcuts import render
from jogo_advinhacao.forms import FormGame
import random

def newNum():
    lista = [i for i in range(100)]
    return random.sample(lista, 1)

def game(data):
    pass

CHANCES = 0
NUM = newNum()

def index(request):
    form = FormGame(request.GET or None)
    if form.is_valid():
        num = NUM

    return render(request, 'index.html', locals())