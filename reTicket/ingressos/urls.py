from django.urls.conf import path
from ingressos import views


app_name = 'ingressos'


urlpatterns = [
  path('lista-ingresso/', views.IngressoListView.as_view(), name='lista-ingresso'),
  path('busca/', views.buscaUmIngresso, name='busca-ingresso'),
  path('retorno-busca/', views.respostaBuscaUmIngresso, name='mostra-ingresso'),
]
