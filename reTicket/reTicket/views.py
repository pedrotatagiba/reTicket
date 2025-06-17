from django.shortcuts import render

from django.contrib.auth.decorators import login_required

@login_required
                
# Create your views here.

def home(request):
# processamento antes de mostrar a home page
    return render(request, 'reTicket/home.html')

def login(request):
    return render(request, 'reTicket/login.html')

def paginaInicial(request):
    return render(request, 'reTicket/inicial.html')

def anuncieSeuIngresso(request):
    return render(request, 'reTicket/anuncieSeuIngresso.html')

def seusIngressos(request):
    return render(request, 'reTicket/seusIngressos.html')

def pesquiseEventos(request):
    return render(request, 'reTicket/pesquiseEventos.html')

def acessaIngressos(request):
    return render(request, 'ingressos/ingressos.html')