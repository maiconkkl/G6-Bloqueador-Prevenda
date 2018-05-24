from django.contrib import admin
from .models import Prevenda
from django import forms


class prevenda(admin.ModelAdmin):
    list_display = ('codigo', 'status')
    status = {1: "Aguardando", 8: "Concluido"}
    readonly_fields = ["prevenda", "codigo"]

admin.site.register(Prevenda, prevenda)
