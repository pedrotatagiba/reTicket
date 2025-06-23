from django.urls import path
from . import views

app_name= 'reTicket'


urlptters = [
    path('busca/', views.buscaItem, name='busca-item'),
    path('retorno-busca/', views.resultadoBuscaItem, name='resultado-busca'),
]
