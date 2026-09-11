# Sistema de Gestión de Proyectos y Tareas (WebApp)

Aplicación web desarrollada con Django para la gestión de proyectos y tareas con autenticación de usuarios, permisos y entorno administrativo personalizado.

## Requisitos
- Python 3.10+
- Virtualenv

## Instalación y Configuración / Clonar el repositorio o descomprimir el proyecto
cd Proyecto_Modulo_6

## Crear y activar entorno virtual
python -m venv venv
.\venv\Scripts\Activate.ps1

## Instalar dependencias
pip install django

## Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate

## Crear un superusuario (Administrador)
python manage.py createsuperuser

## Iniciar el servidor de desarrollo
python manage.py runserver

-------------------------------------------------------------------------

## Ejecución de Pruebas Unitarias
python manage.py test core

-------------------------------------------------------------------------

## Características Principales

Gestión de Autenticación: Registro de usuario, inicio y cierre de sesión seguro.

Control de Proyectos: CRUD completo para proyectos propios de cada usuario.

Gestión de Tareas: Filtros de prioridad, estado, fechas límite e integración con usuarios asignados.

Administración: Panel personalizado en /admin.