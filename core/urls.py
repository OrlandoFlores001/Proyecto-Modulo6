from django.urls import path
from .views import (
    RegistroView,
    DashboardView,
    ProyectosListView,
    ProyectoCreateView,
    ProyectoUpdateView,
    ProyectoDeleteView,
    TareasListView,
    TareaCreateView,
    TareaUpdateView,
    TareaDeleteView,
)

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
    path('', DashboardView.as_view(), name='dashboard'),
    path('proyectos/', ProyectosListView.as_view(), name='proyectos_list'),
    path('proyectos/nuevo/', ProyectoCreateView.as_view(), name='proyecto_create'),
    path('proyectos/<int:pk>/editar/', ProyectoUpdateView.as_view(), name='proyecto_update'),
    path('proyectos/<int:pk>/eliminar/', ProyectoDeleteView.as_view(), name='proyecto_delete'),
    path('proyectos/<int:proyecto_id>/tareas/', TareasListView.as_view(), name='tareas_list'),
    path('proyectos/<int:proyecto_id>/tareas/nueva/', TareaCreateView.as_view(), name='tarea_create'),
    path('tareas/<int:pk>/editar/', TareaUpdateView.as_view(), name='tarea_update'),
    path('tareas/<int:pk>/eliminar/', TareaDeleteView.as_view(), name='tarea_delete'),
]