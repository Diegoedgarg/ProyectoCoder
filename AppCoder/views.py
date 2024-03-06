from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Estudiantes, Curso
# Create your views here.
def padre(request):
 return render(request,"padre.html")

def inicio(request):
 return render(request,"inicio.html")

def ver_estudiantes(request):
 return render (request,"ver_estudiantes.html")

def ver_cursos(request):
 return render (request,"ver_cursos.html")

def ver_profesores(request):
 return render (request,"ver_profesores.html")

def ver_entregable(request):
 return render (request,"ver_entregable.html")

def crear_curso(request):
    curso1 = Curso(nombre="Python", comision = 5020 )
    curso1.save()
    return HttpResponse("Hemos creado un curso")

def crear_estudiante(request):
    Est1 = Estudiantes(1,"Diego", "Gutierrez","diego@gmail.com", 40)
    Est2 = Estudiantes(2,"Maillen", "Cortes","maillen@gmail.com", 30)

    Est1.save()
    Est2.save()
    info = {"n1":Est1.nombre, "n2":Est2.nombre}
    return render (request,"estudiantes.html", info)
