from django import forms
from .models import Curso, Profesor, Clases, Alumno

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class ClasesForm(forms.ModelForm):
    class Meta:
        model = Clases
        fields = '__all__'

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'