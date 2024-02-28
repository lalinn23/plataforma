from django.contrib import admin
from fasesApp.models import Fases


@admin.register(Fases)
class FasesAdmin(admin.ModelAdmin):
    list_display = ['nombreF', 'created_at']