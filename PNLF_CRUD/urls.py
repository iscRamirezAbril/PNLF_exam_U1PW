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
    # Esta es la URL que se utiliza para modificar los datos de un estadio registrado. Aquí, se está tomando de
    # referencia el ID del estadio que se desea modificar (localhost:8000/stadium/1/). Cabe mencionar que
    # tambien se le está dando un nombre a la URL para poder utilizarla en el archivo "stadium_list.html" (name="stadium_Update")
    path('stadiums/update/<int:id>/', views.stadium_form, name='stadium_Update'),
    # Esta es la URL que se utiliza para eliminar un empleado registrado. Aquí, se está tomando de referencia el ID del
    # empleado que se desea eliminar (localhost:8000/employees/1/delete). Cabe mencionar que tambien se le está dando un
    # nombre a la URL para poder utilizarla en el archivo "employee_list.html" (name="delete_employee")
    path('stadiums/delete/<int:id>/', views.stadium_delete, name='stadium_delete')
]