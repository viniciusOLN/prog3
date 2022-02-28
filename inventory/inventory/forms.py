from dataclasses import field
from django import forms
from inventory.models import Product

class FormQuantData(forms.Form):
    quantCompany = forms.IntegerField(label="Quantidade de dados falsos de Empresas", min_value=0)
    quantProduct = forms.IntegerField(label="Quantidade de dados falsos de Produtos", min_value=0)
    quantProductGroup = forms.IntegerField(label="Quantidade de dados falsos de Grupos de Produtos", min_value=0)
    resetData = forms.BooleanField(label="Resetar os dados existentes na tabela?", required=False)

class FormEditProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'unit', 'price', 'active', 'product_group',)