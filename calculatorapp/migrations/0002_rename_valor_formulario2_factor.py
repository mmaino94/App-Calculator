# Generated by Django 4.2.1 on 2023-07-24 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculatorapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formulario2',
            old_name='valor',
            new_name='factor',
        ),
    ]
