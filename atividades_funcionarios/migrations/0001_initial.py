# Generated by Django 5.0.3 on 2024-09-19 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateTimeField(auto_now_add=True)),
                ('data_fim', models.DateField()),
            ],
        ),
    ]
