from django.db import models

from django.contrib.auth.models import User

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
           
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
   
    class Meta:
        verbose_name_plural = "Profesores"
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
        
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
                
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
    
class Avatar(models.Model):
    # vincula la tabla con la tabla de usuarios
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Guardar avatares en la carpeta media/avatares
    imagen = models.ImageField(upload_to='avatares', null = True, blank = True)
    