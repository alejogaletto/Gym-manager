# Generated by Django 4.1.6 on 2023-02-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_student_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
