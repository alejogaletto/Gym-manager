# Generated by Django 4.1.6 on 2023-02-09 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_student_health_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='health_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]