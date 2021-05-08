from django.db import models

# Create your models here.

class Curso(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo del Curso', max_length=50)
    fecha_inicio = models.DateField('Fecha de Inicio', max_length=50)
    fecha_termino = models.DateField('Fecha de Finalización', max_length=50)
    descripcion = models.CharField('Descripción del Curso', max_length=50)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.titulo

class Clases(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo de la Clase', max_length=50)
    descripcion = models.CharField('Descripcion de la Clase', max_length=50)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'

    def __str__(self):
        return self.titulo

class Profesor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del Profesor', max_length=50)
    apellido_paterno = models.CharField('Apellido Paterno', max_length=50)
    apellido_materno = models.CharField('Apellido Materno', max_length=50)
    nacionalidad = models.CharField('Nacionalidad', max_length=50)
    curso = models.ManyToManyField(Curso)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del Alumno', max_length=50)
    apellido_paterno = models.CharField('Apellido Paterno', max_length=50)
    apellido_materno = models.CharField('Apellido Materno', max_length=50)
    nacionalidad = models.CharField('Nacionalidad', max_length=50)
    edad = models.IntegerField('Edad')
    curso = models.ManyToManyField(Curso)

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def __str__(self):
        return self.nombre

class Temas(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo del Tema', max_length=50)
    url_video = models.URLField('URL de la Clase', max_length=50)
    clase = models.ForeignKey(Clases, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

    def __str__(self):
        return self.titulo