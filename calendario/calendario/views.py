from re import template
from django.shortcuts import render
from calendario.forms import FormCalendario
import calendar
            
   
def index(request):
    if request.method == "POST":
    
        form = FormCalendario(request.POST)
        ano = int(form['year'].value())
        mes = int(form['month'].value())
        ano_extenso = {
            "1":"Janeiro",
            "2":"Fevereiro",
            "3":"Março",
            "4":"Abril",
            "5":"Maio",
            "6":"Junho",
            "7":"Julho",
            "8":"Agosto",
            "9":"Setembro",
            "10":"Outubro",
            "11":"Novembro",
            "12":"Dezembro",
        }

        if form.is_valid():
            calendar.setfirstweekday(calendar.SUNDAY)
            value = calendar.monthcalendar(ano, mes)
            context = {
                'form': form,
                'value': value,
                'ano_extenso': ano_extenso[str(mes)][0:3],                
            }
        
            return render(request, 'calendar.html', context=context)

    else:
        form = FormCalendario()
        context = {
            'form': form,
            'value': None
        }
    return render(request, 'index.html', context=context)

