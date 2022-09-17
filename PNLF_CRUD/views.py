# |----- Importación de librerías -----|
from os import name
from django.shortcuts import render, redirect # Se importan las funciones render y redirect de Django
from PNLF_CRUD.forms import * # Se importan todos los formularios del archivo 'forms.py'
from .models import * # Se importan todos los modelos del archivo 'models.py'
from django.contrib import messages

# Create your views here.
# ---------------------------------------------------------------------------------------------- #
# |-------------------| FUNCIONES DE VISTA CORRESPONDIENTES A LOS ESTADIOS |-------------------| #
# ---------------------------------------------------------------------------------------------- #

# Función que se encraga de mostrar la lista de los estadios
def stadium_list(request):
    context = {'stadium_list': Stadium.objects.all()} # Se crea un diccionario con la lista de estadios
    # Se renderiza el archivo 'stadium_list.html' y se le envía el diccionario creado
    return render(request, 'stadiums_CRUD/stadium_list.html', context)

# Función que se encarga de mostrar el formulario para registrar un nuevo estadio
def stadium_form(request, id=0):
    # Si el método de la petición es "GET", se crea un objeto del formulario "stadiumForm" y se envía a la plantilla
    if request.method == "GET":
        if id == 0:
            form = stadiumForm() # Se crea una instancia de la clase 'stadiumForm' que se encuentra en el archivo 'forms.py'
        else:
            stadium = Stadium.objects.get(pk=id) # Se obtiene el estadio que se desea actualizar
            form = stadiumForm(instance=stadium) # Se crea una instancia de la clase 'stadiumForm' que se encuentra en el archivo 'forms.py'
        # Se renderiza el archivo 'stadium_form.html' y se le envía el formulario creado
        return render(request, 'stadiums_CRUD/stadium_form.html', {'form': form})
    
    # Si el método de la petición es "POST", se crea un objeto del formulario "stadiumForm" y se envía a la plantilla
    else:
        if id == 0:
            form = stadiumForm(request.POST) # Se crea una instancia de la clase 'stadiumForm' que se encuentra en el archivo 'forms.py'
        else:
            stadium = Stadium.objects.get(pk=id) # Se obtiene el estadio que se desea actualizar
            form = stadiumForm(request.POST, instance=stadium) # Se crea una instancia de la clase 'stadiumForm' que se encuentra en el archivo 'forms.py'
        if form.is_valid(): # Si el formulario es válido, se procede a guardar los datos en la base de datos
            form.save() # Se guarda el formulario
        messages.success(request, 'El estadio ha sido registrado con éxito.') # Se muestra un mensaje de éxito
        return redirect('/stadiums/list/') # Se redirecciona a la página de la lista de estadios

# Función que se encarga de eliminar un estadio registrado
def stadium_delete(request, id):
    stadium = Stadium.objects.get(pk=id) # Se obtiene el estadio que se desea eliminar
    stadium.delete() # Se elimina el estadio
    messages.success(request, 'El estadio ha sido eliminado correctamente.') # Se muestra un mensaje de éxito
    return redirect('/stadiums/list/') # Se redirecciona a la página de la lista de estadios

# --------------------------------------------------------------------------------------------- #
# |-------------------| FUNCIONES DE VISTA CORRESPONDIENTES A LOS EQUIPOS |-------------------| #
# --------------------------------------------------------------------------------------------- #

# Función que se encarga de mostrar la lista de los equipos
def team_list(request):
    return # render(request, 'PNLF_CRUD/team_list.html')

# Función que se encarga de mostrar el formulario para registrar un nuevo equipo
def team_form(request):
    return # render(request, 'PNLF_CRUD/team_form.html')

# Función que se encarga de eliminar un equipo registrado
def team_delete(request):
    return # render(request, 'PNLF_CRUD/team_delete.html')

# ----------------------------------------------------------------------------------------------- #
# |-------------------| FUNCIONES DE VISTA CORRESPONDIENTES A LOS JUGADORES |-------------------| #
# ----------------------------------------------------------------------------------------------- #

# Función que se encarga de mostrar la lista de los jugadores
def player_list(request):
    return # render(request, 'PNLF_CRUD/player_list.html')

# Función que se encarga de mostrar el formulario para registrar un nuevo jugador
def player_form(request):
    return # render(request, 'PNLF_CRUD/player_form.html')

# Función que se encarga de eliminar un jugador registrado
def player_delete(request):
    return # render(request, 'PNLF_CRUD/player_delete.html')