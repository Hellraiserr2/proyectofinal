# Generated by Django 4.2.2 on 2023-06-28 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallepedido',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='detallepedido',
            name='planta',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='planta',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='DetallePedido',
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.DeleteModel(
            name='Planta',
        ),
    ]