from django.contrib import admin
from ingressos.models import Ingresso

@admin.register(Ingresso)
class IngressoAdmin(admin.ModelAdmin):
    list_display = ('evento', 'codigo', 'dtEvento', 'preco')
    search_fields = ('evento')
    list_filter = ('dtEvento')
