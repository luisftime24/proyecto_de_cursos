from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
# Se importan los modelos y formularios

from .models import Clases, Curso, Alumno, Profesor
from .forms import ProfesorForm, ClasesForm, AlumnoForm, CursoForm

# Create your views here.

def Home(request):
    return render(request, 'index.html')

def crearCurso(request):
    if request.method == 'POST':
        curso_form = CursoForm(request.POST)
        if curso_form.is_valid():
            curso_form.save()
            return redirect('index')
    else:
        curso_form = CursoForm()
    return render(request, 'cursos/crear_curso.html', {'curso_form': curso_form})

def listarCursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/listar_cursos.html', {'cursos': cursos})


def editarCurso(request, id):
    curso_form = None
    error = None
    try:
        curso = Curso.objects.get(id=id)
        if request.method == 'GET':
            curso_form = CursoForm(instance=curso)
        else:
            curso_form = CursoForm(request.POST, instance=curso)
            if curso_form.is_valid():
                curso_form.save()
                return redirect('/cursos/listar_cursos')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'cursos/editar_curso.html', {'curso_form': curso_form, 'error': error})

def eliminarCurso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect('/cursos/listar_cursos')
    return render(request, 'cursos/eliminar_curso.html', {'curso': curso})