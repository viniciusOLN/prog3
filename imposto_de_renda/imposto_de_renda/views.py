from django.shortcuts import render
from imposto_de_renda.forms import FormRenda

def index(request):
    form = FormRenda(request.GET or None)

    return render(request, 'index.html', locals())