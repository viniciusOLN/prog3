from django.shortcuts import render
from django.views import generic, View
from django.shortcuts import render, redirect, reverse
from inventory.forms import FormQuantData, FormEditProduct
from inventory.utils.fake_data import PopulateData
from inventory.models import Company, GroupProduct, Product, Stock

class ProductEditView(View):     
    def get(self, request, *args, **kwargs):

        pk = int(self.kwargs['pk'])
        product_exists = Product.objects.filter(id=pk).exists()
        
        if product_exists:
            product_instance = Product.objects.get(id=pk)
            formProduct = FormEditProduct(instance=product_instance)
            return render(request, 'inventory_product_edit.html', locals())
        else:
            url = '/inventory/products'
            return render(request, 'inventory_product_not_exists.html', locals())

    def post(self, request, *args, **kwargs):      
        pk = int(self.kwargs['pk'])    
        product_instance = Product.objects.get(id=pk)                  
        formProduct = FormEditProduct(request.POST, instance=product_instance)
        if formProduct.is_valid():
            formProduct.save()
            return redirect(reverse('products-list'))       


class ProductListView(generic.ListView):
    model = Product
    template_name = "inventory_products.html"
    context_object_name = "product_list"

def inventory_product_populate(request):
    form = FormQuantData(request.GET or None)
    if form.is_valid(): 
        fakeData = PopulateData(Company, Product, GroupProduct, Stock)  
        data = form.cleaned_data

        if (data['resetData']):
           fakeData.clean_all_data_in_tables()

        fakeData.populate_with_fake_data_company(data['quantCompany'])
        fakeData.populate_with_fake_data_product_group(data['quantProductGroup'])
        fakeData.populate_with_fake_data_product(data['quantProduct'])        
        fakeData.populate_with_fake_data_stock(data['quantProduct'] * data['quantCompany'])     
           
        return redirect(reverse('products-list'))    
    return render(request, 'inventory_populate.html', locals())