from django.db import models
from django.urls import reverse
from megasena.forms import FormSearch

class MegaSenaModel(models.Model):
    contest = models.IntegerField(primary_key=True, verbose_name="Concurso")
    date = models.DateField(verbose_name="Data")
    orb_1 = models.IntegerField(verbose_name="Bola 1")
    orb_2 = models.IntegerField(verbose_name="Bola 2")
    orb_3 = models.IntegerField(verbose_name="Bola 3")
    orb_4 = models.IntegerField(verbose_name="Bola 4")
    orb_5 = models.IntegerField(verbose_name="Bola 5")
    orb_6 = models.IntegerField(verbose_name="Bola 6")

    class Meta:
        verbose_name = 'Sorteio'

    def get_absolute_url(self):
        return reverse("result_detail", args=[str(self.contest)])
    
    def form_search(self):
        return FormSearch()     
    
        

