# Generated by Django 4.0.7 on 2022-09-16 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNLF_CRUD', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_Coach',
            field=models.CharField(default='-', max_length=50, verbose_name='Entrenador del equipo'),
        ),
    ]
