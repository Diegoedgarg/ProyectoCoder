from django.urls import path
from AppCoder.views import *
urlpatterns = [
    path('curso/', crear_curso),
    path('estudiantes/', crear_estudiante),
    path('ver_estudiantes/', ver_estudiantes,name="verestudiantes"),
    path('ver_entregable/', ver_entregable,name="verentregables"),
    path('ver_cursos/', ver_cursos,name="vercursos"),
    path('ver_profesores/', ver_profesores,name="verprofesores"),
    path('', inicio, name="Home"),
]