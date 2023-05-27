from django.shortcuts import render , redirect
from .models import Libros
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required 


# Create your views here.

def home(request):
    Libroslistados =Libros.objects.all()
    return render(request, "gestionLibros.html",{"Libros": Libroslistados})

def registrarLibros(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    existencias=request.POST['numexistentes']

    libro=Libros.objects.create(
    codigo=codigo, nombre=nombre, existencias=existencias)
    messages.success(request, '¡Libro registrado!')
    return redirect('/')


def edicionLibros(request, codigo):
    libro = Libros.objects.get(codigo=codigo) 
    return render(request, "edicionLibros.html", {"libro": libro})



def editarLibros(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    existencias = request.POST['numexistentes']

    libro = Libros.objects.get(codigo=codigo)
    libro.nombre = nombre
    libro.existencias = existencias
    libro.save()
    messages.success(request, '¡Libro actualizado!')

    return redirect('/')


def eliminarLibros(request, codigo):
    libro = Libros.objects.get(codigo=codigo)
    libro.delete()
    messages.success(request, '¡Libro eliminado!')

    return redirect('/')

def contacto(request):
    return render(request, "contacto.html")



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Credenciales inválidas')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = AuthenticationForm()
    return render(request, 'base.html', {'form': form})

