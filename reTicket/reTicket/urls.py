# reTicket/reTicket/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views # Mantenha esta linha para as views do projeto reTicket
from ingressos import views as ingressos_views # Adicione esta linha para importar as views do app ingressos

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="root"),
    path("home/", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("inicial/", views.paginaInicial, name="inicial"),

    # --- Ajustes nas URLs de Anunciar e Meus Ingressos ---
    # Aponte 'anuncie_seu_ingresso/' diretamente para a view de criação de ingresso
    path("anuncie_seu_ingresso/", ingressos_views.criarIngresso, name="anuncie"),
    # Aponte 'seus_ingressos/' diretamente para a view de listagem dos ingressos do usuário
    path("seus_ingressos/", ingressos_views.MeusIngressosListView.as_view(), name="meus-ingressos-do-projeto"), # Dê um nome diferente para evitar conflito com 'ingressos'
                                                                                                                   # ou remova o 'name="ingressos"' anterior se não for mais usado
    # --- Mantenha esta linha para incluir as outras URLs do app ingressos (lista, busca, atualiza)
    path('ingressos/', include('ingressos.urls')),

    path("eventos/", views.pesquiseEventos, name="eventos"),
    path("acessaIngressos/", views.acessaIngressos, name="acessaIngressos"),
    path("accounts/", include('django.contrib.auth.urls')),
]