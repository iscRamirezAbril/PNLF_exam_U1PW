"""examU1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# Importar de django.urls el path e include
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # |--------------------------------------------------|
    # |-----------------| NUEVAS RUTAS |-----------------|
    # |--------------------------------------------------|
    
    # -----> Ruta #1: 'home' <----- #
    # Agregamos la ruta 'home' que apunta a la aplicación PNLF_CRUD y a su archivo urls.py, la cual será "http://127.0.0.1:8000/home/”
    path('home/', include('PNLF_CRUD.urls')),
    # -----> Ruta #2: 'stadiums' <----- #
    # Agregamos la ruta 'stadiums' que apunta a la aplicación PNLF_CRUD y a su archivo urls.py, la cual será "http://127.0.0.1:8000/stadiums/"
    path('stadiums/', include('PNLF_CRUD.urls')),
    # -----> Ruta #3: 'teams' <----- #
    # Agregamos la ruta 'teams' que apunta a la aplicación PNLF_CRUD y a su archivo urls.py, la cual será "http://127.0.0.1:8000/teams/"
    path('teams/', include('PNLF_CRUD.urls')),
    # -----> Ruta #4: 'players' <----- #
    # Agregamos la ruta 'players' que apunta a la aplicación PNLF_CRUD y a su archivo urls.py, la cual será "http://127.0.0.1:8000/players/"
    path('players/', include('PNLF_CRUD.urls')),
]
