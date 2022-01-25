from django.shortcuts import render
from imposto_de_renda.forms import FormRenda

def calc(data):
    dependent = data['dependents'] * 2
    ir = data['annual_income'] - (data['annual_income'] * dependent/100)    

    if ir >= 0 and ir < 2000:
        imp = '0,00'
    elif ir >= 2000 and ir < 5000:
        imp = data['annual_income'] * 5/100
    elif ir >= 5000 and ir < 10000:
        imp = data['annual_income'] * 10/100
    elif ir >= 10000:
        imp = data['annual_income'] * 15/100
    return (ir, imp)
        
def index(request):
    form = FormRenda(request.GET or None)
    if form.is_valid():
        imp = calc(form.cleaned_data)
        template_name = 'result.html'
    else:
        template_name = 'index.html'

    return render(request, template_name, locals())