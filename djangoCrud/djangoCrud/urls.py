
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    #path('tasks/', views.helloWorld, name='tasks'),
    path('inscribirse/', views.inscribirse, name='inscribirse'),
    path('tareas/', views.tarea, name='tareas'),
    path('tareas_Completado/', views.tarea_completa, name='tarea_completadas'),
    path('tarea/crear/', views.crearTarea, name='crearTarea'),
    path('tarea/<int:tarea_id>/', views.detallesTarea, name='detallesTarea'),
    path('tarea/<int:tarea_id>/completado', views.completadaTarea, name='completadaTarea'),
    path('tarea/<int:tarea_id>/eliminado', views.eliminadaTarea, name='eliminadaTarea'),
    path('cerrarSesion/', views.cerrarSesion, name='cerraSesion'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion')
]
