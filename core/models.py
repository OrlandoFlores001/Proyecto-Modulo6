from django.db import models
from django.conf import settings

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='proyectos')
    creado = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completada', 'Completada'),
    ]
    PRIORIDADES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]
    
    titulo = models.CharField(max_length=200) 
    
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas') 
    
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    prioridad = models.CharField(max_length=10, choices=PRIORIDADES, default='media')
    fecha_limite = models.DateField()
    asignado_a = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='tareas_asignadas')

    def __str__(self):
        return self.titulo