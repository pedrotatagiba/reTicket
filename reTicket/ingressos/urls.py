from django.urls.conf import path
from ingressos import views


app_name = 'ingressos'


urlpatterns = [
  path('lista-ingresso/', views.IngressoListView.as_view(), name='lista-ingresso'),
  path('atualiza/<int:pk>/', views.IngressoUpdateView.as_view(), name='atualiza-ingresso'),
  path('', views.IngressoListView.as_view(), name='home-ingressos'),
  path('busca/', views.buscaUmIngresso, name='busca-ingresso'),
  path('retorno-busca/', views.respostaBuscaUmIngresso, name='mostra-ingresso'),
]
