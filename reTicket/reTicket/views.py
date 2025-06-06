from django.shortcuts import render

# Create your views here.

def home(request):
# processamento antes de mostrar a home page
    return render(request, 'reTicket/home.html')