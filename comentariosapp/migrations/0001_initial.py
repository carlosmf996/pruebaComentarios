# Generated by Django 4.2.7 on 2023-11-13 12:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.TextField()),
                ('comentario', models.TextField()),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
