# Generated by Django 5.0.3 on 2024-03-28 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0009_rename_barrio1_año2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Año2015',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barrio', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
                ('mes', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Año2016',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barrio', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
                ('mes', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Año2017',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barrio', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
                ('mes', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Año2018',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barrio', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
                ('mes', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Año2019',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barrio', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
                ('mes', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Año2020',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barrio', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
                ('mes', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Año2021',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barrio', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
                ('mes', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Año2022',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barrio', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
                ('mes', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Año2023',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barrio', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
                ('mes', models.CharField(max_length=120)),
            ],
        ),
    ]
