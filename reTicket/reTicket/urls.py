# reTicket/reTicket/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views # Mantenha esta linha para as views do projeto reTicket
from ingressos import views as ingressos_views # Adicione esta linha para importar as views do app ingressos

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="root"),
    path("home/", views.home, name="home"),
    # REMOVA OU COMENTE ESTA LINHA: path("login/", views.login, name="login"),
    path("inicial/", views.paginaInicial, name="inicial"),

    path("anuncie_seu_ingresso/", ingressos_views.criarIngresso, name="anuncie"),
    path("seus_ingressos/", ingressos_views.MeusIngressosListView.as_view(), name="meus-ingressos-do-projeto"),
    path('ingressos/', include('ingressos.urls')),

    path("eventos/", views.pesquiseEventos, name="eventos"),
    path("acessaIngressos/", views.acessaIngressos, name="acessaIngressos"),
    # Mantenha esta linha, pois ela inclui todas as URLs de autenticação do Django, incluindo o login correto:
    path("accounts/", include('django.contrib.auth.urls')),
]