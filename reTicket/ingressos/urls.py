from django.urls.conf import path
from ingressos import views


app_name = 'ingressos'


urlpatterns = [
  path('busca/', views.buscaUmIngresso, name='busca-ingresso'),
  path('retorno-busca/', views.respostaBuscaUmIngresso, name='mostra-ingresso'),
]
