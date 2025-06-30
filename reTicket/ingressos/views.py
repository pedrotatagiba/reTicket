# reTicket/ingressos/views.py
from django.shortcuts import render, get_object_or_404, redirect # Adicione 'redirect'
from django.views.generic.base import View
from ingressos.forms import IngressoModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from ingressos.models import Evento
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator # Para aplicar decoradores a Class-Based Views
from django.contrib.auth.mixins import LoginRequiredMixin # Para mixin de login em CBV

# --- Nova View para Criar Evento ---
@login_required # Garante que apenas usuários logados possam criar eventos
def criarIngresso(request):
    if request.method == 'POST':
        formulario = IngressoModel2Form(request.POST)
        if formulario.is_valid():
            evento = formulario.save(commit=False) # Não salva ainda para associar o usuário
            evento.user = request.user # Associa o evento ao usuário logado
            evento.save()
            return HttpResponseRedirect(reverse_lazy("ingressos:meus-ingressos")) # Redireciona para os próprios ingressos
    else:
        formulario = IngressoModel2Form()
    contexto = {'formulario': formulario}
    return render(request, 'ingressos/criaIngresso.html', contexto) # Criaremos este template

# --- Modificação da View de Atualização ---
@method_decorator(login_required, name='dispatch') # Garante login e aplica a métodos da CBV
class IngressoUpdateView(View):
  def get(self, request, pk, *args, **kwargs):
    evento = get_object_or_404(Evento, pk=pk)
    # Verifica se o usuário logado é o proprietário do evento
    if evento.user != request.user:
        return redirect('ingressos:home-ingressos') # Redireciona se não for o proprietário (ou para outra página de erro/acesso negado)

    formulario = IngressoModel2Form(instance=evento)
    contexto = {'evento': formulario, 'evento_obj': evento} # Adicionado 'evento_obj' para acesso ao objeto no template
    return render(request, 'ingressos/atualizaIngresso.html', contexto)
   
  def post(self, request, pk, *args, **kwargs):
    evento = get_object_or_404(Evento, pk=pk)
    # Verifica novamente antes de salvar
    if evento.user != request.user:
        return redirect('ingressos:home-ingressos') # Redireciona se não for o proprietário

    formulario = IngressoModel2Form(request.POST, instance=evento)
    if formulario.is_valid():
      evento = formulario.save()  
      # evento.save() # Não é necessário chamar save() novamente aqui, formulario.save() já faz isso
      return HttpResponseRedirect(reverse_lazy("ingressos:meus-ingressos")) # Redireciona para os próprios ingressos após atualização
    else:
      contexto = {'evento': formulario, 'evento_obj': evento}
      return render(request, 'ingressos/atualizaIngresso.html', contexto)

# --- Modificação da View de Listagem de Todos os Eventos ---
@method_decorator(login_required, name='dispatch')
class IngressoListView(View):
  def get(self, request, *args, **kwargs):
    eventos = Evento.objects.all().order_by('-dtEvento') # Ordena por data do evento
    contexto = { 'eventos': eventos, }
    return render(request, 'ingressos/listaIngressos.html', contexto)
  
# --- Nova View para Listar Apenas os Eventos do Usuário Logado ---
@method_decorator(login_required, name='dispatch')
class MeusIngressosListView(View):
    def get(self, request, *args, **kwargs):
        # Filtra os eventos pelo usuário logado
        eventos_do_usuario = Evento.objects.filter(user=request.user).order_by('-dtEvento')
        contexto = {'eventos': eventos_do_usuario}
        return render(request, 'ingressos/meusIngressos.html', contexto) # Criaremos este template

# --- Views existentes que não precisam de alteração para este requisito ---
def buscaUmIngresso(request):
  return render(request, 'ingressos/buscaUmIngresso.html')


def respostaBuscaUmIngresso(request):
  eventos = Evento.objects.all().filter(
    nome__icontains=request.GET.get('nome'))
  contexto = { 'eventos': eventos, }
  return render(request, 'ingressos/listaIngressos.html', contexto)