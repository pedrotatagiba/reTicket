from django.shortcuts import render
from .models import Ingresso  

def buscaItem(request):
    return render(request, 'ingressos/buscaItem.html')

def resultadoBuscaItem(request):
    busca = request.GET.get('evento')
    resultados = Evento.objects.filter(nome__icontains=busca)
    contexto = {'resultados': resultados}
    return render(request, 'ingressos/resultadoBusca.html', contexto)

