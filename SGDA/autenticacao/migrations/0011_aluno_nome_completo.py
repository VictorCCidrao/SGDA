# Generated by Django 5.0.4 on 2024-04-11 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("autenticacao", "0010_remove_aluno_nome_completo"),
    ]

    operations = [
        migrations.AddField(
            model_name="aluno",
            name="nome_completo",
            field=models.CharField(blank=True, default="", max_length=100, null=True),
        ),
    ]