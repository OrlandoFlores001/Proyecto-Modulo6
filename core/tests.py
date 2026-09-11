from datetime import date, timedelta
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Proyecto, Tarea

class ModelosTestCase(TestCase):
    def setUp(self):
        # Crear usuario de prueba
        self.user = User.objects.create_user(
            username='testuser', 
            password='Password123!'
        )
        # Crear proyecto de prueba
        self.proyecto = Proyecto.objects.create(
            nombre='Proyecto de Prueba',
            descripcion='Descripción del proyecto de prueba',
            propietario=self.user
        )

    def test_creacion_proyecto(self):
        """Verifica que el proyecto se cree correctamente y que el __str__ funcione."""
        self.assertEqual(str(self.proyecto), 'Proyecto de Prueba')
        self.assertEqual(self.proyecto.propietario, self.user)

    def test_creacion_tarea(self):
        """Verifica la creación de una tarea asociada al proyecto."""
        tarea = Tarea.objects.create(
            titulo='Tarea 1',
            descripcion='Descripción de la tarea 1',
            proyecto=self.proyecto,
            estado='pendiente',
            prioridad='alta',
            fecha_limite=date.today() + timedelta(days=5),
            asignado_a=self.user
        )
        self.assertEqual(str(tarea), 'Tarea 1')
        self.assertEqual(tarea.proyecto, self.proyecto)
        self.assertEqual(tarea.estado, 'pendiente')


class VistasTestCase(TestCase):
    def setUp(self):
        # Crear usuario y autenticarlo
        self.user = User.objects.create_user(
            username='testuser', 
            password='Password123!'
        )
        self.client.login(username='testuser', password='Password123!')
        
        # Crear proyecto inicial
        self.proyecto = Proyecto.objects.create(
            nombre='Proyecto Demo',
            descripcion='Descripción Demo',
            propietario=self.user
        )

    def test_dashboard_view_autenticado(self):
        """Verifica que el usuario logueado acceda al dashboard correctamente."""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/dashboard.html')
        self.assertContains(response, 'Proyecto Demo')

    def test_crear_proyecto_view(self):
        """Verifica la creación de un nuevo proyecto vía POST."""
        response = self.client.post(reverse('proyecto_create'), {
            'nombre': 'Proyecto Nuevo',
            'descripcion': 'Descripción del nuevo proyecto'
        })
        self.assertEqual(response.status_code, 302)  # Redirección exitosa
        self.assertTrue(Proyecto.objects.filter(nombre='Proyecto Nuevo').exists())

    def test_crear_tarea_view(self):
        """Verifica la creación de una tarea vinculada a un proyecto."""
        url = reverse('tarea_create', kwargs={'proyecto_id': self.proyecto.id})
        fecha_futura = date.today() + timedelta(days=2)
        
        response = self.client.post(url, {
            'titulo': 'Tarea Creada en Test',
            'descripcion': 'Probando el formulario de tarea',
            'estado': 'pendiente',
            'prioridad': 'media',
            'fecha_limite': fecha_futura,
            'asignado_a': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Tarea.objects.filter(titulo='Tarea Creada en Test').exists())