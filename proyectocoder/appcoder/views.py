from django.shortcuts import render, redirect
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import *
from .forms import *

def busqueda_rapida(request, tabla):    # version Q
    if request.method == "POST":
        buscar = request.POST["elemento"]
        resultado = tabla.objects.filter( Q(nombre__icontains=buscar) | Q(camada__icontains=buscar) ).values()
        return resultado

def inicio(request):
    try:
        avatar = Avatar.objects.get(user=request.user)
    except:
        avatar =  None
    return render(request, "appcoder/inicio.html", {"avatar": avatar})

def cursos(request):
    cursos = Curso.objects.all()
    ctx = {"cursos": cursos, "buscar": busqueda_rapida(request, Curso)}
    return render(request, "appcoder/cursos/cursos.html", ctx)

@login_required
def crear_curso(request):
    if request.method == "POST":
        form = NuevoCurso(request.POST)
        if form.is_valid:
            form.save()
            return redirect('cursos')
    else: 
        form = NuevoCurso()
    ctx = {"form": form}
    return render(request, "appcoder/cursos/nuevo_curso.html", ctx)
    
    
# Aplicando formulario con herencia de modelo
    
def profesores(request):
    profesores = Profesor.objects.all()
    ctx = {"profesores": profesores}
    return render(request, "appcoder/profesores/profesores.html", ctx)

@login_required
def crear_profesor(request):
    if request.method == "POST":
        form = NuevoProfesor(request.POST)
        if form.is_valid:
            form.save()
            return redirect('profesores')
    else: 
        form = NuevoProfesor()
    ctx = {"form": form}
    return render(request, "appcoder/profesores/nuevo_profesor.html", ctx)

@login_required
def modificar_profesor(request, profesor_id):
    profesor = Profesor.objects.get(id=profesor_id)
    if request.method == "POST":
        form = NuevoProfesor(request.POST, instance=profesor)
        if form.is_valid:       
            form.save()
            return redirect('profesores')
    form = NuevoProfesor(instance=profesor)                 # muestro lo datos cargados del profesor a modificar
    ctx = {"form": form}
    return render(request, "appcoder/profesores/nuevo_profesor.html", ctx)
    
@login_required
def eliminar_profesor(request, profesor_id):
    profesor = Profesor.objects.get(id=profesor_id)    
    profesor.delete()
    return redirect ('profesores')

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    ctx = {"estudiantes": estudiantes}
    return render(request, "appcoder/estudiantes/estudiantes.html", ctx)

@login_required
def crear_estudiante(request):
    if request.method == "POST":
        form = NuevoEstudiante(request.POST)
        if form.is_valid:
            form.save()
            return redirect('estudiantes')
    else: 
        form = NuevoEstudiante()
    ctx = {"form": form}
    return render(request, "appcoder/estudiantes/nuevo_estudiante.html", ctx)

# Aplicando CBV

class EntregableList(ListView):
    model = Entregable
    template_name = "appcoder/entregables/entregables.html"
    
class EntregableDetalle(DetailView):
    model = Entregable
    template_name = "appcoder/entregables/entregable_detalle.html"
    
class EntregableCrear(LoginRequiredMixin, CreateView):
    model = Entregable
    success_url = "/appcoder/entregable/list"
    template_name = "appcoder/entregables/entregable_form.html"
    fields = '__all__'
    
class EntregableModificar(LoginRequiredMixin, UpdateView):
    model = Entregable
    success_url = "/appcoder/entregable/list"
    template_name = "appcoder/entregables/entregable_form.html"
    fields = '__all__'
    
class EntregableBorrar(LoginRequiredMixin, DeleteView):
    model = Entregable
    template_name = "appcoder/entregables/entregable_confirm_delete.html"
    success_url = "/appcoder/entregable/list"     
    
# LOGIN / LOGOUT: directamente por urls.py

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username = usuario, password = contra)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                return redirect('Login')
        else:
            return redirect('Login')
    form = AuthenticationForm()
    ctx = {"form": form}
    return render(request, "appcoder/registro/login.html", ctx)  

# USUARIOS

def register(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'appcoder/inicio.html', {"mensaje": "Usuario creado!!!"})    
    else:
        form = UserRegisterForm()
    return render(request,"appcoder/registro/registro.html", {"form": form})

def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid:       
            form.save()
            return redirect('inicio')
    form = UserEditForm(instance=usuario)                 # muestro lo datos cargados del profesor a modificar
    ctx = {"form": form}
    return render(request, "appcoder/registro/editar_perfil.html", ctx)    