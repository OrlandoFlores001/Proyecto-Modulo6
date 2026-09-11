from django.contrib import admin
from .models import Proyecto, Tarea

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'propietario', 'creado')
    search_fields = ('nombre', 'propietario__username')
    list_filter = ('propietario', 'creado')
    date_hierarchy = 'creado'

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'proyecto',
        'estado',
        'prioridad',
        'asignado_a',
        'fecha_limite'
    )
    search_fields = ('titulo', 'descripcion', 'proyecto__nombre')
    list_filter = ('estado', 'prioridad', 'proyecto', 'asignado_a')
    list_editable = ('estado', 'prioridad')
    date_hierarchy = 'fecha_limite'
