from re import template
from django.shortcuts import render
from calendario.forms import FormCalendario
import calendar
            
   
def index(request):
    if request.method == "POST":
    
        form = FormCalendario(request.POST)
        ano = int(form['year'].value())
        mes = int(form['month'].value())

        if form.is_valid():
            calendar.setfirstweekday(calendar.SUNDAY)
            value = calendar.monthcalendar(ano, mes)
            context = {
                'form': form,
                'value': value
            }
        
            return render(request, 'index.html', context=context)

    else:
        form = FormCalendario()
        context = {
            'form': form,
            'value': None
        }
    return render(request, 'index.html', context=context)

