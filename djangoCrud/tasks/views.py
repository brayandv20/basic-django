from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import formularioTarea
from .models import Tareas
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html',{
    })

def inscribirse(request):

    if request.method == 'GET':
        return render(request, 'inscribirse.html',{
            'form': UserCreationForm
        })
        #print("Enviando formulario")
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #Register user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')

                """return render(request, 'inscribirse.html',{
                    'form': UserCreationForm,
                    'confirmation' : "Usuario creado con exito"
                })"""
            except IntegrityError:

                return render(request, 'inscribirse.html',{
                    'form' : UserCreationForm,
                    'error': 'EL usuario ya existe'
                })

        return render(request, 'inscribirse.html',{
            'form' : UserCreationForm,
            'error' : 'Las contraseñas no coinciden'
        })

@login_required
def tarea(request):
    Tarea = Tareas.objects.filter(usuario=request.user, diaCompletado__isnull=True)   
    return render(request, 'tareas.html', {'Tarea': Tarea})

@login_required
def tarea_completa(request):
    Tarea = Tareas.objects.filter(usuario=request.user, diaCompletado__isnull=False).order_by('diaCompletado')
    return render(request, 'tareas.html', {'Tarea': tarea})

@login_required
def crearTarea(request):
    if request.method == 'GET':
        return render(request, 'crearTarea.html',{
            'form': formularioTarea
        }) 
        print("Estoy dando error")
    else:
        try:
            form = formularioTarea(request.POST)
            nuevaTarea = form.save(commit=False)
            nuevaTarea.usuario = request.user
            nuevaTarea.save()
            print(nuevaTarea)
            #print(form)
            print(request.POST)
            return redirect('tareas')

            """return render(request, 'crearTarea.html',{
                'form': formularioTarea
            })"""  

        except ValueError:
            return render(request, 'crearTarea.html',{
                'form': formularioTarea,
                'error': 'Estoy dando error'
            })

@login_required
def detallesTarea(request, tarea_id):
    if request.method == 'GET':
        tarea = get_object_or_404(Tareas, pk=tarea_id, usuario=request.user)
        form = formularioTarea(instance=tarea)
        return render(request, 'detallesTarea.html', {'tarea': tarea, 'form': form})
    else:
        try:
            #print(request.POST)
            #return render(request, 'detallesTarea.html', {'tarea': tarea, 'form': form})
            tarea = get_object_or_404(Tareas, pk = tarea_id)
            form = formularioTarea(request.POST, instance=tarea, usuario=request.user)
            form.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'detallesTarea.html',{'tarea': tarea, 'form': form, 'error': 'huvo un problema no se pudo actualizar'})

@login_required
def completadaTarea(request, tarea_id):
    tarea = get_object_or_404(Tareas, pk=tarea_id, usuario=request.user)
    if request.method == 'POST':
        tarea.diaCompletado = timezone.now()
        tarea.save()
        return redirect('tareas')

@login_required
def eliminadaTarea(request, tarea_id):
    tarea = get_object_or_404(Tareas, pk=tarea_id, usuario=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tareas')

@login_required
def cerrarSesion(request):
    #return render(request, 'cerrarSesion.html')
    logout(request)
    return redirect('home')


def iniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'iniciarSesion.html',{
            'form': AuthenticationForm
        })
    else: 
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciarSesion.html',{
                'form': AuthenticationForm,
                'error':'Usuario o contraseña es incorrecta'
            })
        else:
            login(request, user)
            return redirect('tareas')
            print(request.POST)

