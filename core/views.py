from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, TemplateView, ListView, UpdateView, DeleteView
)

from .models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm, RegistroUsuarioForm


class RegistroView(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'core/registration/registro.html'
    success_url = reverse_lazy('login')


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyectos'] = Proyecto.objects.filter(propietario=self.request.user)
        return context


class ProyectosListView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'core/proyecto_list.html'
    context_object_name = 'proyectos'

    def get_queryset(self):
        return Proyecto.objects.filter(propietario=self.request.user)


class ProyectoCreateView(LoginRequiredMixin, CreateView):
    form_class = ProyectoForm
    template_name = 'core/proyecto_form.html'
    success_url = reverse_lazy('proyectos_list')

    def form_valid(self, form):
        form.instance.propietario = self.request.user
        return super().form_valid(form)


class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'core/proyecto_form.html'
    success_url = reverse_lazy('proyectos_list')

    def get_queryset(self):
        return Proyecto.objects.filter(propietario=self.request.user)


class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = 'core/proyecto_confirm_delete.html'
    success_url = reverse_lazy('proyectos_list')

    def get_queryset(self):
        return Proyecto.objects.filter(propietario=self.request.user)


# --- TAREAS ---
class TareasListView(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'core/tarea_list.html'
    context_object_name = 'tareas'

    def get_queryset(self):
        return Tarea.objects.filter(
            proyecto_id=self.kwargs['proyecto_id'],
            proyecto__propietario=self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyecto'] = get_object_or_404(
            Proyecto, id=self.kwargs['proyecto_id'], propietario=self.request.user
        )
        return context


class TareaCreateView(LoginRequiredMixin, CreateView):
    form_class = TareaForm
    template_name = 'core/tarea_form.html'

    def form_valid(self, form):
        proyecto = get_object_or_404(
            Proyecto, id=self.kwargs['proyecto_id'], propietario=self.request.user
        )
        form.instance.proyecto = proyecto
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'tareas_list', kwargs={'proyecto_id': self.kwargs['proyecto_id']}
        )


class TareaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'core/tarea_form.html'

    def get_queryset(self):
        return Tarea.objects.filter(proyecto__propietario=self.request.user)

    def get_success_url(self):
        return reverse_lazy(
            'tareas_list', kwargs={'proyecto_id': self.object.proyecto.id}
        )


class TareaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'core/tarea_confirm_delete.html'

    def get_queryset(self):
        return Tarea.objects.filter(proyecto__propietario=self.request.user)

    def get_success_url(self):
        return reverse_lazy(
            'tareas_list', kwargs={'proyecto_id': self.object.proyecto.id}
        )