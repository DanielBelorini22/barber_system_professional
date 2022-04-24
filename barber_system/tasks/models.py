from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Task(models.Model):
    STATUS_CHOICES = (
        ('doing', 'Doing'),
        ('done', 'Done')
    )

    title = models.CharField('Título', max_length=255, blank=False)
    description = models.TextField('Descrição')
    done = models.CharField('Status', max_length=9, choices=STATUS_CHOICES)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title


class Corte(models.Model):
    DURACAO_CHOICES = (
        ('1', '00:30'),
        ('2', '01:00'),
        ('3', '01:30'),
        ('4', '02:00')
    )
    NOME_CHOICES = (
        ('corte', 'Corte'),
        ('barba', 'Barba'),
        ('sobrancelha', 'Sobrancelha'),
        ('corte_sobrancelha', 'Corte e sobrancelha'),
        ('corte_barba', 'Corte e barba'),
        ('barba_sobrancelha', 'Barba e Sobrancelha'),
        ('corte_barba_sobrancelha', 'Corte,barba e sobrancelha'),
    )

    nome = models.CharField('Nome', max_length=255, null=False, blank=False, choices=NOME_CHOICES)
    duracao = models.CharField('Duração', max_length=50, null=False, blank=False, choices=DURACAO_CHOICES)
    preco = models.FloatField('Preço', null=False, blank=False, validators=[MinValueValidator(0.0)])
