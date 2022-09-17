# |----- Importación de librerías -----|
from django.db import models # Importamos el módulo models de django.db
from pyexpat import model # Importamos el módulo models de pyexpat

# Create your models here.

# |---------------------------------|
# |----- DECLARACIÓN DE CLASES -----|
# |---------------------------------|

# |----- CLASE #1: Position -----|
# Clase que almacenará la información (id y nombre) de las posiciones disponibles para los jugaores
class Position(models.Model):
    pos_Name =              models.CharField(max_length = 100, verbose_name = "Nombre de la posición")

    def __str__ (self):
        return self.pos_Name
    
# |----- CLASE #2: Stadium -----|
class Stadium(models.Model):
    stdm_Name =             models.CharField(max_length = 50, verbose_name = "Nombre del estadio", null = False)
    stdm_City =             models.CharField(max_length = 20, verbose_name = "Ciudad del estadio", null = False)
    stdm_State =            models.CharField(max_length = 20, verbose_name = "Estado del estadio", null = False)
    stdm_Capacity =         models.IntegerField(verbose_name = "Capacidad del estadio", null = False)

    def __str__ (self):
        return self.stdm_Name
    
# |----- CLASE #3: Team -----|
# Clase que almacenará la información (id, nombre, ciudad, estado, país y año de fundación, entre otros) de los equipos
class Team(models.Model):
    team_Name =             models.CharField(max_length = 50, verbose_name = "Nombre del equipo", null = False) # Nombre del equipo
    team_City =             models.CharField(max_length = 50, verbose_name = "Ciudad del equipo", null = False) # Ciudad del equipo
    team_State =            models.CharField(max_length = 50, verbose_name = "Estado del equipo") # Estado del equipo
    team_Country =          models.CharField(max_length = 50, verbose_name = "País del equipo") # País del equipo
    team_University =       models.CharField(max_length = 50, verbose_name = "Universidad del equipo", null = False, default='-') # Universidad del equipo
    team_FoundationYear =   models.IntegerField(verbose_name = "Año de fundación del equipo", null = False) # Año de fundación del equipo
    team_nMembers =         models.IntegerField(verbose_name = "Número de miembros del equipo", null = False) # Número de miembros del equipo
    team_Coach =            models.CharField(max_length = 50, verbose_name = "Entrenador del equipo", null = False, default='-') # Entrenador del equipo
    team_Victories =        models.IntegerField(verbose_name = "Número de victorias del equipo", null = False) # Número de victorias del equipo
    team_Defeats =          models.IntegerField(verbose_name = "Número de derrotas del equipo", null = False) # Número de derrotas del equipo
    team_Status =           models.BooleanField(verbose_name = "Estado del equipo") # Estado del equipo
    # |----- Relación de la clase Team con la clase Stadium -----|
    team_Stadium =          models.ForeignKey(Stadium, on_delete = models.CASCADE, verbose_name = "Estadio del equipo", null = False) # Estadio del equipo
    
    def __str__ (self):
        return self.team_Name

# |----- CLASE #4: Member -----|
# Clase que almacenará la información (id, nombre, apellido, edad, posición, equipo, entre otros) de los miembros o jugadores de los equipos
class Player(models.Model):
    player_Name =           models.CharField(max_length = 50, verbose_name = "Nombre del jugador", null = False) # Nombre del jugador
    player_LastName =       models.CharField(max_length = 50, verbose_name = "Apellido del jugador", null = False) # Apellido del jugador
    player_Birthdate =      models.DateField(verbose_name = "Fecha de nacimiento del jugador", null = False) # Fecha de nacimiento del jugador
    player_citizenShip =    models.CharField(max_length = 50, verbose_name = "Nacionalidad del jugador", null = False) # Nacionalidad del jugador
    player_Status =         models.BooleanField(verbose_name = "Estado del jugador", null = False) # Estado del jugador
    player_Number =         models.IntegerField(verbose_name = "Número del jugador", null = False) # Número del jugador
    player_JoinDate =       models.DateField(verbose_name = "Fecha de ingreso del jugador") # Fecha de ingreso del jugador
    # |----- Relación de la clase Player con la clase Team -----|
    player_Team =           models.ForeignKey(Team, on_delete = models.CASCADE, verbose_name = "Equipo del jugador", null = False) # Equipo del jugador
    # |----- Relación de la clase Player con la clase Position -----|
    player_Position =       models.ForeignKey(Position, on_delete = models.CASCADE, verbose_name = "Posición del jugador", null = False) # Posición del jugador