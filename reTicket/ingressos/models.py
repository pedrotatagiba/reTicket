from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=100, help_text='Evento:')
    codigo = models.IntegerField(help_text='Código do ingresso:')
    dtEvento = models.DateField(help_text='Data do evento no formato DD/MM/AAAA:')
    preco = models.DecimalField(help_text='Preço:', decimal_places=2, max_digits=8)
	
    def __str__(self):
        return self.nome

