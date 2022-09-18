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

class teamForm(forms.ModelForm):
    # class Meta: Se utiliza para definir los atributos de la clase "stadiumForm".
    class Meta:
        model = Team # Se indica el modelo al que pertenece el formulario
        # Se definen los campos que se mostrarán en el formulario
        fields = (
            'team_Name', 
            'team_City', 
            'team_State', 
            'team_University',
            'team_FoundationYear',
            'team_nMembers',
            'team_Coach',
            'team_Victories',
            'team_Defeats',
            'team_Status',
            'team_Stadium') # Se definen los campos que se mostrarán en el formulario
        
        # Se establecen etiquetas para los campos del formulario
        labels = {
            'team_Name': 'Nombre del equipo',
            'team_City': 'Ciudad',
            'team_State': 'Estado',
            'team_University': 'Universidad',
            'team_FoundationYear': 'Año de fundación',
            'team_nMembers': 'Número de miembros',
            'team_Coach': 'Entrenador',
            'team_Victories': 'Victorias',
            'team_Defeats': 'Derrotas',
            'team_Status': 'Estado',
            'team_Stadium': 'Estadio'
        }

class playerForm(forms.ModelForm):
    # class Meta: Se utiliza para definir los atributos de la clase "stadiumForm".
    class Meta:
        model = Player # Se indica el modelo al que pertenece el formulario
        # Se definen los campos que se mostrarán en el formulario
        fields = (
            'player_Name', 
            'player_LastName', 
            'player_Birthdate', 
            'player_citizenShip',
            'player_Status',
            'player_Number',
            'player_JoinDate',
            'player_Team',
            'player_Position') # Se definen los campos que se mostrarán en el formulario
        
        # Se establecen etiquetas para los campos del formulario
        labels = {
            'player_Name': 'Nombre del jugador',
            'player_LastName': 'Apellido del jugador',
            'player_Birthdate': 'Fecha de nacimiento (Ej. October 25, 1987)',
            'player_citizenShip': 'Nacionalidad',
            'player_Status': 'Estado',
            'player_Number': 'Número',	
            'player_JoinDate': 'Fecha de ingreso (Ej. October 25, 1987)',
            'player_Team': 'Equipo',
            'player_Position': 'Posición'
        }