from django.contrib import admin
from clientesApp.models import Clientes

# Register your models here.

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ['nombreC', 'published']



