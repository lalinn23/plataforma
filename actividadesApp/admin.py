from django.contrib import admin
from actividadesApp.models import Actividad


@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ['lider', 'user', 'created_at', 'proyecto', 'actividad', 'fase', 'etapa', 'descripcion', 'hora']
