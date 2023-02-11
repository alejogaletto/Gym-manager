# Generated by Django 4.1.6 on 2023-02-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_exercise_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='link',
            field=models.CharField(max_length=100, null=True, verbose_name='Link de video'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='muscle',
            field=models.CharField(max_length=30, null=True, verbose_name='Músculo'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(max_length=30, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='dni',
            field=models.IntegerField(max_length=8, null=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='health_file',
            field=models.FileField(null=True, upload_to='', verbose_name='Ficha médica'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='last_name',
            field=models.CharField(max_length=30, null=True, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=30, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone',
            field=models.IntegerField(max_length=15, null=True, verbose_name='Teléfono'),
        ),
    ]