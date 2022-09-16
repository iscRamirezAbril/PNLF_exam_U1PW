# |----- Importación de librerías -----|
from cProfile import label
from django import forms # Se importan los formularios de Django
from . models import * # Se importa el modelo Employee del archivo models.py

class stadiumForm(forms.ModelForm):
    # class Meta: Se utiliza para definir los atributos de la clase "stadiumForm".
    class Meta:
        model = Stadium # Se indica el modelo al que pertenece el formulario
        # Se definen los campos que se mostrarán en el formulario
        fields = (
            'stdm_Name', 
            'stdm_City', 
            'stdm_State', 
            'stdm_Capacity') # Se definen los campos que se mostrarán en el formulario
        
        # Se establecen etiquetas para los campos del formulario
        labels = {
            'stdm_Name': 'Nombre del estadio',
            'stdm_City': 'Ciudad',
            'stdm_State': 'Estado',
            'stdm_Capacity': 'Capacidad'
        }
