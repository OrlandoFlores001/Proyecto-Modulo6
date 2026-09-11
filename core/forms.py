from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Proyecto, Tarea
from datetime import date

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = [
            'titulo',
            'descripcion',
            'estado',
            'prioridad',
            'fecha_limite',
            'asignado_a'
        ]
        widgets = {
            'fecha_limite': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'prioridad': forms.Select(attrs={'class': 'form-select'}),
            'asignado_a': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_fecha_limite(self):
        fecha_limite = self.cleaned_data.get('fecha_limite')
        if fecha_limite and fecha_limite < date.today():
            raise forms.ValidationError(
                "La fecha límite no puede ser anterior a la fecha de hoy."
            )
        return fecha_limite