from django.contrib import admin

from .models import *

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'camada')

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'profesion')
    
class EntregableAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_de_entrega', 'entregado')


admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Entregable, EntregableAdmin)
admin.site.register(Avatar)

