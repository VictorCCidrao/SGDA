# Generated by Django 5.0.4 on 2024-04-11 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0002_nutricionista_delete_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='nome_completo',
            field=models.CharField(default='', max_length=100),
        ),
    ]
