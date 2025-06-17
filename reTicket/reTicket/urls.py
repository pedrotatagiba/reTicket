"""
URL configuration for reTicket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from reTicket import views
from django.urls.conf import include

urlpatterns = [
    
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('login/',views.login, name='login'),
    path('inicial/',views.paginaInicial, name='inicial'),
    path('anuncie_seu_ingresso/',views.anuncieSeuIngresso, name='anuncie'),
    path('seus_ingressos/',views.seusIngressos, name='ingressos'),
    path('eventos/',views.pesquiseEventos, name='eventos'),
    path('ingressos/',views.acessaIngressos , name='acessaIngressos'),
    path('accounts/', include('django.contrib.auth.urls')),

]


