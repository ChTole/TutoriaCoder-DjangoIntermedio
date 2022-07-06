from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #Login / Logout
    path('login', views.login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name='appcoder/logout.html'), name='Logout'),
    #Registro
    path('register', views.register, name="Register"),
    path('editarPerfil', views.editar_perfil, name="EditarPerfil"),
    #Vistas
    path('', views.inicio, name = "inicio"),
    path('cursos', views.cursos, name = "cursos"),
    path('crear_curso', views.crear_curso, name = "crear_curso"),
    path('profesores', views.profesores, name = "profesores"),
    path('crear_profesor', views.crear_profesor, name = "crear_profesor"),
    path('eliminar_profesor/<profesor_id>', views.eliminar_profesor, name = "eliminar_profesor"),
    path('modificar_profesor/<profesor_id>', views.modificar_profesor, name = "modificar_profesor"),
    path('estudiantes', views.estudiantes, name = "estudiantes"),
    path('crear_estudiante', views.crear_estudiante, name = "crear_estudiante"),
    
    # Aplicando CBV
    path('entregable/list', views.EntregableList.as_view(), name='list'),
    path('entregable_detalle/<pk>', views.EntregableDetalle.as_view(), name='Detail'),
    # reemplazo el regex (o expresión regular) por una dirección (arbitraria)
    # <pk> luego de la barra representa <modelo_id> del otro método
    # <pk>  =  primary key  =  id de la tabla correspondiente
    path('entregable_formulario/', views.EntregableCrear.as_view(), name='New'),
    path('entregable_formulario/<pk>', views.EntregableModificar.as_view(), name='Edit'),
    path('entregable_borrar/<pk>', views.EntregableBorrar.as_view(), name='Delete'),   
]