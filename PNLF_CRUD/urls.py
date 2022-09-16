from importlib.resources import path
from unittest.mock import patch
from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns = [
    # Esta es la URL que corresponde a la visualización de los estadios registrados. Esta URL manda a llamar a la función
    # 'stadium_list' que se encuentra en el archivo 'views.py' de la aplicación 'PNLF_CRUD'. 
    path('stadiums/list/', views.stadium_list, name='stadium_List'),
    # Esta URL corresponde al formulario de registro o actualización de un estadio. Esta URL manda a llamar a la función
    # 'stadium_form' que se encuentra en el archivo 'views.py' de la aplicación 'PNLF_CRUD'.
    path('stadiums/form/', views.stadium_form, name='stadium_Form'),
]
