from django.contrib import admin
from .models import Tareas

class tareaAdmin(admin.ModelAdmin):
    readonly_fields = ("diaCompletado", )
# Register your models here.

admin.site.register(Tareas, tareaAdmin)

