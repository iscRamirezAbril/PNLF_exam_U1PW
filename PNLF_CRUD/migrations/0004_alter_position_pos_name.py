# Generated by Django 4.0.7 on 2022-09-16 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNLF_CRUD', '0003_alter_player_player_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='pos_Name',
            field=models.CharField(max_length=100, verbose_name='Nombre de la posición'),
        ),
    ]