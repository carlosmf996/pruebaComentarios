# Generated by Django 4.2.7 on 2023-11-14 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentariosapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='published_date',
        ),
    ]