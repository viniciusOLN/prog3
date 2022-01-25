from django.contrib import admin
from django.urls import path
from imposto_de_renda.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
