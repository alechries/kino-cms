# Generated by Django 3.1.5 on 2021-01-20 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminLte', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='slug',
        ),
    ]