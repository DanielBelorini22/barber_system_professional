# Generated by Django 4.0.3 on 2022-05-24 19:06

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_corte'),
    ]

    operations = [
        migrations.AddField(
            model_name='corte',
            name='observacao',
            field=models.TextField(default=str, max_length=200, verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='corte',
            name='status',
            field=models.CharField(choices=[('agendado', 'Agendado'), ('efetuado', 'Efetuado'), ('cancelado', 'Cancelado')], default='agendado', max_length=25, verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='tipocorte',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AddField(
            model_name='tipocorte',
            name='atualizado_em',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tipocorte',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipocorte',
            name='desconto',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Desconto'),
        ),
        migrations.AlterField(
            model_name='corte',
            name='cliente',
            field=models.CharField(max_length=100, verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='tipocorte',
            name='duracao',
            field=models.SmallIntegerField(choices=[('1', '00:30'), ('2', '01:00'), ('3', '01:30'), ('4', '02:00')], verbose_name='Duração'),
        ),
    ]
