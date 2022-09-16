from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'pos_Name']

@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ['stdm_Name', 'stdm_City', 'stdm_State', 'stdm_Capacity']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_Name', 'team_City', 'team_State', 'team_Country', 'team_FoundationYear', 'team_nMembers', 'team_Coach', 'team_Victories', 'team_Defeats', 'team_Status', 'team_Stadium']

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['player_Name', 'player_LastName', 'player_Birthdate', 'player_citizenShip', 'player_Status', 'player_Number', 'player_JoinDate', 'player_Team', 'player_Position']
    