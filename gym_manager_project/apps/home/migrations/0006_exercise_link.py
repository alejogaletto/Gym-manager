# Generated by Django 4.1.6 on 2023-02-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_staff_health_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]