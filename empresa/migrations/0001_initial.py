# Generated by Django 4.1.7 on 2023-03-23 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Empresa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("logo", models.ImageField(upload_to="logo_empresa")),
                ("nome", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254)),
                ("cidade", models.CharField(max_length=30)),
                ("endereco", models.CharField(max_length=60)),
                (
                    "nicho_mercado",
                    models.CharField(
                        choices=[
                            ("M", "Marketing"),
                            ("N", "Nutrição"),
                            ("D", "Design"),
                        ],
                        max_length=3,
                    ),
                ),
                ("caracteristica_empresa", models.TextField()),
            ],
            options={"verbose_name": "Empresa", "verbose_name_plural": "Empresas",},
        ),
        migrations.CreateModel(
            name="Tecnologias",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tecnologia", models.CharField(max_length=30)),
            ],
            options={
                "verbose_name": "Tecnologia",
                "verbose_name_plural": "Tecnologias",
            },
        ),
        migrations.CreateModel(
            name="Vagas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=30)),
                (
                    "nivel_experiencia",
                    models.CharField(
                        choices=[("J", "Júnior"), ("P", "Pleno"), ("S", "Sênior")],
                        max_length=2,
                    ),
                ),
                ("data_final", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("I", "Interesse"),
                            ("C", "Currículo enviado"),
                            ("E", "Entrevista"),
                            ("D", "Desafio técnico"),
                            ("F", "Finalizado"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="empresa.empresa",
                    ),
                ),
                (
                    "tecnologias_dominadas",
                    models.ManyToManyField(to="empresa.tecnologias"),
                ),
                (
                    "tecnologias_estudar",
                    models.ManyToManyField(
                        related_name="estudar", to="empresa.tecnologias"
                    ),
                ),
            ],
            options={"verbose_name": "Vaga", "verbose_name_plural": "Vagas",},
        ),
        migrations.AddField(
            model_name="empresa",
            name="tecnologias",
            field=models.ManyToManyField(to="empresa.tecnologias"),
        ),
    ]
