from django.urls import path
from inventory.views import inventory_product_populate, ProductListView, ProductEditView

urlpatterns = [
    path('populate', inventory_product_populate),    
    path('products', ProductListView.as_view(), name='products-list'),    
    path('product/<int:pk>', ProductEditView.as_view(), name='product-edit')
]
