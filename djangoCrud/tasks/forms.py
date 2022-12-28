from django import forms
from django.forms import ModelForm
from .models import Tareas

class formularioTarea(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = ['titulo','descripcion','importante'] 
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Escriba el titulo'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Escriba el descripcion'}),
            #'importante' : forms.CheckboxInput()
        }