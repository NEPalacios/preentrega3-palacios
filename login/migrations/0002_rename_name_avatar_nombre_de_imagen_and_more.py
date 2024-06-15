# Generated by Django 5.0.6 on 2024-06-12 00:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='name',
            new_name='nombre_de_imagen',
        ),
        migrations.AlterField(
            model_name='avatar',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='avatar', to='login.usuario'),
        ),
    ]