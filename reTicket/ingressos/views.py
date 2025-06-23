from django.shortcuts import render
from ingressos.models import Ingresso
from django.contrib.auth.decorators import login_required


def buscaUmIngresso(request):
  return render(request, 'ingressos/buscaUmIngresso.html')


def respostaBuscaUmIngresso(request):
  evento = Ingresso.objects.all().filter(
    evento__icontains=request.GET.get('evento'))
  contexto = { 'evento': evento, }
  return render(request, 'ingressos/listaIngressos.html', contexto)
