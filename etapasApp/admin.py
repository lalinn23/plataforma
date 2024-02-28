from django.contrib import admin
from etapasApp.models import Etapa


@admin.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    list_display = ['nombreE', 'created_at']