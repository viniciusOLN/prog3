from unicodedata import name
from django.urls import path
from megasena.views import index, loadfile, results, resultDetail, contest

urlpatterns = [
    path('', index),
    path('loadfile', loadfile, name="loadfile"),
    path('megasena', results.as_view(), name="results"),
    path('megasena/<int:pk>', resultDetail.as_view(), name="result_detail"), 
    path('megasena/', contest, name="contest"),       
] 
