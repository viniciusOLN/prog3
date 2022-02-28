from enum import unique
from django.db import models
from django.urls import reverse

def fformat(n, dec=2, tsep='.', dsep=','):
    s = f'{n:0.{dec}f}'
    t = s.split('.')
    ls = list(t[0])

    for i in range(len(t[0]))[::-3][1:]:
        ls.insert(i + 1,tsep)
    s = ''.join(ls) + dsep + t[1]

    return s

class GroupProduct(models.Model):
    '''Modelo representando o grupo do produto'''
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=50, help_text= "Digite aqui o nome do grupo do produto", verbose_name="Nome do grupo")
    active = models.BooleanField(default=True, help_text= "", verbose_name="Ativo")

    class Meta:
        verbose_name = 'Grupo de um produto'
        verbose_name_plural = 'Grupos de Produtos'

    def __str__(self):
        return self.name

class Product(models.Model):
    '''Modelo representando o produto'''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, help_text="Nome do produto", default='', verbose_name="Nome do produto")
    unit = models.CharField(max_length=15, help_text="Quantidade de unidades do produto", default=0, verbose_name="Unidades do produto")
    price = models.FloatField(default=0.00, verbose_name="Preço do produto")
    active = models.BooleanField(default=True, verbose_name="Ativo")
    product_group = models.ForeignKey(GroupProduct, on_delete=models.SET_NULL, null=True, verbose_name="Grupo do produto")

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name

    def display_price_formated(self):
        return fformat(self.price)
    
    def generate_url(self):
        return reverse('product-edit', args=[str(self.id)])

class Company(models.Model):
    '''Modelo representando a companhia'''
    id = models.CharField(primary_key=True, max_length=5, default='', help_text="Identificador Único para a Empresa")
    name = models.CharField(max_length=80, verbose_name="Nome da companhia", default='', help_text="Nome da Empresa")
    phone = models.CharField(max_length=11, verbose_name="Telefone", default='', help_text="Telefone da Empresa")
    mail = models.CharField(max_length=50, verbose_name="Email", default='', help_text="Email da Empresa")
    site = models.CharField(max_length=100, verbose_name="Site", default='', help_text="Site da Empresa")

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.name

class Stock(models.Model):
    '''Modelo representando o estoque da companhia'''
    quantity = models.IntegerField(verbose_name="Quantidade", default=0, help_text="Quantidade do produto no estoque")
    last_update = models.DateTimeField(verbose_name="Última Atualização", default='', help_text="Última atualização sobre o produto no estoque")
    product_in_stock = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name="Produto em estoque")
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name="Empresa")

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'

    def __str__(self):
        return str(self.quantity)