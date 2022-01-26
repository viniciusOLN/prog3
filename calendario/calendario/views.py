from re import template
from django.shortcuts import render
from calendario.forms import FormCalendario
from calendar import monthrange
import calendar
            
# def getDayCalendar(data):
#     name = calendar.day_name[data]

#     if(name in "Monday"):
#         return 'SE'          
#     elif(name in "Tuesday"):
#         return 'T'          
#     elif(name in "Wednesday"):
#         return 'QA'          
#     elif(name in "Thursday"):
#         return 'QI'          
#     elif(name in "Friday"):
#         return 'SX'          
#     elif(name in "Saturday"):
#         return 'SA'          
#     elif(name in "Sunday"):
#         return 'D'          
    
def index(request):
    if request.method == "POST":
        # week = ['D',' S'  ,'T'  ,'Q',  'Q',  'S',  'S' ]
        # days = [('D', []), ('SE', []), ('T', []), ('QA', []), ('QI', []), ('SX', []), ('SA', [])]

        form = FormCalendario(request.POST)
        ano = int(form['year'].value())
        mes = int(form['month'].value())

        if form.is_valid():
            
            value = calendar.month(ano, mes)
            
            # f, n = monthrange(ano, mes)

            # day_first = getDayCalendar(f)
            # for index, day in enumerate(days):
            #     print(index, day[1])
            #     if day[0] == day_first:
            #         days[1].append(1)
            #         second = index+1
            #         print(second)
            #         break

            # print(days)    
            # num = 2
            # print(n)
            # for index, element in enumerate(days, start=second):
            #     print(index, element)

            #     days[1].append(num)
            #     num = num + 1
            #     if(element[0] == 'SA'):
            #         element = days
            #     if(num == int(n)):
            #         break    
            # print(days)

            template_name = 'index.html'
        else:
            template_name = 'index.html'
    else:
        form = FormCalendario()
        template_name = 'index.html'

    return render(request, template_name, locals())

