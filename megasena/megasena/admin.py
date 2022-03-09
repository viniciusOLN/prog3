from django.contrib import admin
from megasena.models import MegaSenaModel

class ContestAdmin(admin.ModelAdmin):
    list_display = ('contest', 'date', 'orb_1', 'orb_2', 'orb_3', 'orb_4', 'orb_5', 'orb_6',)


admin.site.register(MegaSenaModel, ContestAdmin)
