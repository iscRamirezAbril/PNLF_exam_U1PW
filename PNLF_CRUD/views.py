from django.shortcuts import render

# Create your views here.
# ---------------------------------------------------------------------------------------------- #
# |-------------------| FUNCIONES DE VISTA CORRESPONDIENTES A LOS ESTADIOS |-------------------| #
# ---------------------------------------------------------------------------------------------- #

# Función que se encraga de mostrar la lista de los estadios
def stadium_list(request):
    return render(request, 'stadiums_CRUD/stadium_list.html')

# Función que se encarga de mostrar el formulario para registrar un nuevo estadio
def stadium_form(request):
    return render(request, 'stadiums_CRUD/stadium_form.html')

# Función que se encarga de eliminar un estadio registrado
def stadium_delete(request):
    return # render(request, 'PNLF_CRUD/stadium_delete.html')

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