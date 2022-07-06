from django.test import TestCase
from .models import Curso

class CursoTest(TestCase):
    def setUp(self):
        Curso.objects.create(nombre = "Python", camada = 1)
        
    def test_curso_nombre(self):
        curso = Curso.objects.get(camada = 1)
        self.assertEqual(curso.nombre, "Python")
