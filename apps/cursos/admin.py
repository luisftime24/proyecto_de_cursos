from django.contrib import admin
from .models import Curso, Profesor, Clases, Alumno
# Register your models here.

class cursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descripcion')

class profesorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido_paterno', 'apellido_materno')

class clasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')

class alumnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido_paterno', 'apellido_materno')
    

admin.site.register(Curso, cursoAdmin)
admin.site.register(Profesor, profesorAdmin)
admin.site.register(Clases, clasesAdmin)
admin.site.register(Alumno, alumnoAdmin)