# Generated by Django 2.1.2 on 2018-11-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Busqueda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('Todos', 'Todas las marcas'), ('Suzuki', 'Suzuki'), ('Hiunday', 'Hiunday')], default='Todos', max_length=50)),
            ],
        ),
    ]
