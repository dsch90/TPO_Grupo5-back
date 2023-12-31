# Generated by Django 4.2.3 on 2023-07-12 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automovil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_automovil', models.CharField(max_length=100)),
                ('descripcion_automovil', models.CharField(max_length=100)),
                ('precio_automovil', models.IntegerField()),
                ('marca_automovil', models.CharField(max_length=100)),
                ('categoria_automovil', models.IntegerField()),
                ('estado_automovil', models.IntegerField()),
                ('foto_automovil', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_salida_reserva', models.DateTimeField(auto_now_add=True)),
                ('horario_regreso_reserva', models.CharField(max_length=100)),
                ('usuario_reserva', models.IntegerField()),
                ('estado_reserva', models.IntegerField()),
                ('vehiculo_reserva', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('correo_usuario', models.CharField(max_length=100)),
                ('contacto_usuario', models.CharField(max_length=100)),
                ('direccion_usuarios', models.CharField(max_length=100)),
                ('password_usuario', models.CharField(max_length=100)),
            ],
        ),
    ]
