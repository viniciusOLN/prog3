from csv import list_dialects
from django.contrib import admin
from inventory.models import GroupProduct, Product, Stock, Company


class GroupProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    ordering = ('name', 'active')
    search_fields = ("name__startswith", )
    list_filter = ('name', 'active') 

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'preço', 'unit', 'product_group', 'active')
    ordering = ('name', 'price')
    search_fields = ("name__startswith", "price__startswith", "active__startswith")
    list_filter = ('name', 'price', 'product_group')

    def preço(self, obj):        
        return 'R$ ' + obj.display_price_formated()


class StockAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'last_update', 'product_in_stock', 'company')
    ordering = ('quantity', 'last_update')
    search_fields = ("quantity__startswith", "last_update__startswith", "company__startswith")
    list_filter = ('last_update', 'product_in_stock', 'company')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'mail', 'site')
    ordering = ('id', 'name')
    search_fields = ("name__startswith", "mail__startswith")
    list_filter = ('name', 'mail', 'site')


admin.site.register(GroupProduct, GroupProductAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Company, CompanyAdmin)
