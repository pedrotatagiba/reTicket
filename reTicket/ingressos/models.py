# reTicket/ingressos/models.py
from django.db import models
from django.contrib.auth.models import User # Importe o modelo User

class Evento(models.Model):
    # Adicione esta linha:
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventos_criados', null=True, blank=True)
    nome = models.CharField(max_length=100)
    codigo = models.IntegerField()
    dtEvento = models.DateField(help_text='Data do evento no formato DD/MM/AAAA:')
    preco = models.DecimalField(decimal_places=2, max_digits=8)
	
    def __str__(self):
        return self.nome