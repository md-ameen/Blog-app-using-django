# Generated by Django 4.0.3 on 2022-03-11 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='imafe',
            new_name='image',
        ),
    ]