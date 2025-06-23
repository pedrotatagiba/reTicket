from django.contrib import admin
from ingressos.models import Ingresso

@admin.register(Ingresso)
class IngressoAdmin(admin.ModelAdmin):
    list_filter = ['dtEvento']
    search_fields = ['evento']
