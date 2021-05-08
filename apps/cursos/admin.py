from django.contrib import admin
from .models import Curso, Profesor, Clases, Alumno, Temas
# Register your models here.

class cursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descripcion')

class profesorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido_paterno', 'apellido_materno')

class clasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')

class alumnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido_paterno', 'apellido_materno')

class temasAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'url_video')
    

admin.site.register(Curso, cursoAdmin)
admin.site.register(Profesor, profesorAdmin)
admin.site.register(Clases, clasesAdmin)
admin.site.register(Alumno, alumnoAdmin)
admin.site.register(Temas, temasAdmin)