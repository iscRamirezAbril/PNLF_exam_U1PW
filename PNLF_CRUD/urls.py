from importlib.resources import path
from unittest.mock import patch
from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns = [
    # |-------------------------------------------------------------------------------|
    # |-------------------| RUTAS CORRESPONDIENTES A LOS ESTADIOS |-------------------|
    # |-------------------------------------------------------------------------------|
    # Esta es la URL que corresponde a la visualización de los estadios registrados. Esta URL manda a llamar a la función
    # 'stadium_list' que se encuentra en el archivo 'views.py' de la aplicación 'PNLF_CRUD'. 
    path('stadiums/list/', views.stadium_list, name='stadium_List'),
    # Esta URL corresponde al formulario de registro o actualización de un estadio. Esta URL manda a llamar a la función
    # 'stadium_form' que se encuentra en el archivo 'views.py' de la aplicación 'PNLF_CRUD'.
    path('stadiums/form/', views.stadium_form, name='stadium_Form'),
    # Esta es la URL que se utiliza para modificar los datos de un estadio registrado. Aquí, se está tomando de
    # referencia el ID del estadio que se desea modificar (localhost:8000/stadium/1/). Cabe mencionar que
    # tambien se le está dando un nombre a la URL para poder utilizarla en el archivo "stadium_list.html" (name="stadium_Update")
    path('stadiums/update/<int:id>/', views.stadium_form, name='stadium_Update'),
    # Esta es la URL que se utiliza para eliminar un empleado registrado. Aquí, se está tomando de referencia el ID del
    # empleado que se desea eliminar (localhost:8000/team/1/delete). Cabe mencionar que tambien se le está dando un
    # nombre a la URL para poder utilizarla en el archivo "stadium_list.html" (name="stadium_delete")
    path('stadiums/delete/<int:id>/', views.stadium_delete, name='stadium_Delete'),
    
    # |------------------------------------------------------------------------------|
    # |-------------------| RUTAS CORRESPONDIENTES A LOS EQUIPOS |-------------------|
    # |------------------------------------------------------------------------------|
    # Esta es la URL que corresponde a la visualización de los estadios registrados. Esta URL manda a llamar a la función
    # 'team_list' que se encuentra en el archivo 'views.py' de la aplicación 'PNLF_CRUD'. 
    path('teams/list/', views.team_list, name='team_List'),
    # Esta URL corresponde al formulario de registro o actualización de un estadio. Esta URL manda a llamar a la función
    # 'team_form' que se encuentra en el archivo 'views.py' de la aplicación 'PNLF_CRUD'.
    path('teams/form/', views.team_form, name='team_Form'),
    # Esta es la URL que se utiliza para modificar los datos de un estadio registrado. Aquí, se está tomando de
    # referencia el ID del estadio que se desea modificar (localhost:8000/team/1/). Cabe mencionar que
    # tambien se le está dando un nombre a la URL para poder utilizarla en el archivo "stadium_list.html" (name="team_Update")
    path('teams/update/<int:id>/', views.team_form, name='team_Update'),
    # Esta es la URL que se utiliza para eliminar un empleado registrado. Aquí, se está tomando de referencia el ID del
    # empleado que se desea eliminar (localhost:8000/team/1/delete). Cabe mencionar que tambien se le está dando un
    # nombre a la URL para poder utilizarla en el archivo "team_list.html" (name="team_Delete")
    path('teams/delete/<int:id>/', views.team_delete, name='team_Delete'),
    
    # |--------------------------------------------------------------------------------|
    # |-------------------| RUTAS CORRESPONDIENTES A LOS JUGADORES |-------------------|
    # |--------------------------------------------------------------------------------|
    # Esta es la URL que corresponde a la visualización de los estadios registrados. Esta URL manda a llamar a la función
    # 'player_list' que se encuentra en el archivo 'views.py' de la aplicación 'PNLF_CRUD'. 
    path('players/list/', views.player_list, name='player_List'),
    # Esta URL corresponde al formulario de registro o actualización de un estadio. Esta URL manda a llamar a la función
    # 'player_form' que se encuentra en el archivo 'views.py' de la aplicación 'PNLF_CRUD'.
    path('players/form/', views.player_form, name='player_Form'),
    # Esta es la URL que se utiliza para modificar los datos de un estadio registrado. Aquí, se está tomando de
    # referencia el ID del estadio que se desea modificar (localhost:8000/player/1/). Cabe mencionar que
    # tambien se le está dando un nombre a la URL para poder utilizarla en el archivo "player_list.html" (name="player_Update")
    path('players/update/<int:id>/', views.player_form, name='player_Update'),
    # Esta es la URL que se utiliza para eliminar un empleado registrado. Aquí, se está tomando de referencia el ID del
    # empleado que se desea eliminar (localhost:8000/player/1/delete). Cabe mencionar que tambien se le está dando un
    # nombre a la URL para poder utilizarla en el archivo "player_list.html" (name="player_Delete")
    path('players/delete/<int:id>/', views.player_delete, name='player_Delete')
]