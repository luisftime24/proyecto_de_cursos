from django.urls import path
from .views import crearCurso, listarCursos, eliminarCurso, editarCurso


urlpatterns = [
    path('crear_curso/', crearCurso, name='crear_curso'),
    path('listar_cursos/', listarCursos, name='listar_cursos'),
    path('editar_curso/<int:id>', editarCurso, name='editar_curso'), 
    path('eliminar_curso/<int:id>', eliminarCurso, name='eliminar_curso'),       
]