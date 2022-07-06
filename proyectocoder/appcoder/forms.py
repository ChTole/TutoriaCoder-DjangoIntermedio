from django import forms
from .models import Curso, Estudiante, Profesor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NuevoEstudiante(forms.ModelForm):
    class Meta:                         
        model = Estudiante              # de models.py
        fields = ('nombre', 'apellido', 'email')    # los campos que quiero que contenga
        
class NuevoProfesor(forms.ModelForm):
    class Meta:                         
        model = Profesor              # de models.py
        fields = ('nombre', 'apellido', 'email', 'profesion')    # los campos que quiero que contenga
        
class NuevoCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('nombre', 'camada', 'profesor')
        
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña:', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Quita mensajes de ayuda
        help_texts = {k:"" for k in fields}
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar e-m@il:")
    password1 = forms.CharField(label='Contraseña:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña:', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        # Quita mensajes de ayuda
        help_texts = {k:"" for k in fields}
        