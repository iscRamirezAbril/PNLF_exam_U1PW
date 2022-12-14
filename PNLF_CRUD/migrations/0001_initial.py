# Generated by Django 4.0.7 on 2022-09-16 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos_Name', models.CharField(max_length=20, verbose_name='Nombre de la posición')),
            ],
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdm_Name', models.CharField(max_length=50, verbose_name='Nombre del estadio')),
                ('stdm_City', models.CharField(max_length=20, verbose_name='Ciudad del estadio')),
                ('stdm_State', models.CharField(max_length=20, verbose_name='Estado del estadio')),
                ('stdm_Capacity', models.IntegerField(verbose_name='Capacidad del estadio')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_Name', models.CharField(max_length=50, verbose_name='Nombre del equipo')),
                ('team_City', models.CharField(max_length=50, verbose_name='Ciudad del equipo')),
                ('team_State', models.CharField(max_length=50, verbose_name='Estado del equipo')),
                ('team_Country', models.CharField(max_length=50, verbose_name='País del equipo')),
                ('team_FoundationYear', models.IntegerField(verbose_name='Año de fundación del equipo')),
                ('team_nMembers', models.IntegerField(verbose_name='Número de miembros del equipo')),
                ('team_Victories', models.IntegerField(verbose_name='Número de victorias del equipo')),
                ('team_Defeats', models.IntegerField(verbose_name='Número de derrotas del equipo')),
                ('team_Status', models.BooleanField(verbose_name='Estado del equipo')),
                ('team_Stadium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PNLF_CRUD.stadium', verbose_name='Estadio del equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_Name', models.CharField(max_length=50, verbose_name='Nombre del jugador')),
                ('player_LastName', models.CharField(max_length=50, verbose_name='Apellido del jugador')),
                ('player_Birthdate', models.DateField(verbose_name='Fecha de nacimiento del jugador')),
                ('player_citizenShip', models.CharField(max_length=50, verbose_name='Nacionalidad del jugador')),
                ('player_Status', models.BooleanField(verbose_name='Estado del jugador')),
                ('player_Number', models.IntegerField(verbose_name='Número del jugador')),
                ('player_JoinDate', models.DateField(verbose_name='Fecha de ingreso del jugador')),
                ('player_Position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PNLF_CRUD.position', verbose_name='Posición del miembro')),
                ('player_Team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PNLF_CRUD.team', verbose_name='Equipo del miembro')),
            ],
        ),
    ]
