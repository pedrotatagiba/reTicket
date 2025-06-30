from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from ingressos.forms import IngressoModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from ingressos.models import Evento
from django.contrib.auth.decorators import login_required



class IngressoUpdateView(View):
  def get(self, request, pk, *args, **kwargs):
    evento = Evento.objects.get(pk=pk)
    formulario = IngressoModel2Form(instance=evento)
    contexto = {'evento': formulario, }
    return render(request, 'ingressos/atualizaIngresso.html', contexto)
   
  def post(self, request, pk, *args, **kwargs):
    evento = get_object_or_404(Evento, pk=pk)
    formulario = IngressoModel2Form(request.POST, instance=evento)
    if formulario.is_valid():
      evento = formulario.save()  
      evento.save()   
      return HttpResponseRedirect(reverse_lazy("ingressos:lista-ingresso"))
    else:
      contexto = {'evento': formulario, }
      return render(request, 'ingressos/atualizaIngresso.html', contexto)

class IngressoListView(View):
  def get(self, request, *args, **kwargs):
    eventos = Evento.objects.all()
    contexto = { 'eventos': eventos, }
    return render(request, 'ingressos/listaIngressos.html', contexto)
  
def buscaUmIngresso(request):
  return render(request, 'ingressos/buscaUmIngresso.html')


def respostaBuscaUmIngresso(request):
  eventos = Evento.objects.all().filter(
    nome__icontains=request.GET.get('nome'))
  contexto = { 'eventos': eventos, }
  return render(request, 'ingressos/listaIngressos.html', contexto)


