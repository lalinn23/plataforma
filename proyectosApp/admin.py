from django.contrib import admin
from proyectosApp.models import Proyecto


# Register your models here.

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['nombreP','cliente']