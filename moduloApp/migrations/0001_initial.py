# Generated by Django 4.1.7 on 2023-05-11 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreBodega', models.CharField(max_length=50)),
                ('direccionBodega', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCliente', models.CharField(max_length=50)),
                ('telefonoCliente', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('descripcionProducto', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='tipoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoProducto', models.CharField(max_length=100)),
                ('descripcionTipoProducto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProyecto', models.CharField(max_length=50)),
                ('descripcionProyecto', models.CharField(max_length=100)),
                ('estadoProyecto', models.CharField(max_length=100)),
                ('id_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloApp.cliente')),
                ('id_Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloApp.producto')),
            ],
        ),
        migrations.CreateModel(
            name='productoBodega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('id_Bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloApp.bodega')),
                ('id_Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloApp.producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='idTipoProducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloApp.tipoproducto'),
        ),
    ]