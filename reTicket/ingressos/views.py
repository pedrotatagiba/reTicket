from django.shortcuts import render
from ingressos.models import Ingresso
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View

def buscaUmIngresso(request):
  return render(request, 'ingressos/buscaUmIngresso.html')

def respostaBuscaUmIngresso(request):
  evento = Ingresso.objects.all().filter(
    evento__icontains=request.GET.get('evento'))
  contexto = { 'evento': evento, }
  return render(request, 'ingressos/listaIngressos.html', contexto)

class IngressoListView(View):
 def get(self, request, *args, **kwargs):
  ingressos = Ingresso.objects.all()
  contexto = { 'ingressos': ingressos, }
  return render(request, 'ingressos/listaIngressos.html', contexto)
