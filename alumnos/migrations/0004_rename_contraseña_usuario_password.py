# Generated by Django 4.2.2 on 2023-06-28 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='password',
        ),
    ]
