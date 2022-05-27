from django.conf import settings
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


DURACAO_CHOICES = (
    (1, '00:30'),
    (2, '01:00'),
    (3, '01:30'),
    (4, '02:00')
)


class TipoCorte(models.Model):
    NOME_CHOICES = (
        ('corte', 'Corte'),
        ('barba', 'Barba'),
        ('sobrancelha', 'Sobrancelha'),
        ('corte_sobrancelha', 'Corte e sobrancelha'),
        ('corte_barba', 'Corte e barba'),
        ('barba_sobrancelha', 'Barba e sobrancelha'),
        ('corte_barba_sobrancelha', 'Corte, barba e sobrancelha'),
    )

    nome = models.CharField('Nome', max_length=255, null=False, blank=False, choices=NOME_CHOICES)
    duracao = models.SmallIntegerField('Duração', null=False, blank=False, choices=DURACAO_CHOICES)
    preco = models.FloatField('Preço', null=False, blank=False, validators=[MinValueValidator(0.0)])
    desconto = models.FloatField('Desconto', null=True, validators=[MinValueValidator(0.0)])
    ativo = models.BooleanField('Ativo', default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.get_nome_display()} - {self.get_duracao_display()}'

    def get_ativo_display(self):
        return 'Sim' if self.ativo else 'Não'


class Corte(models.Model):
    STATUS_CHOICES = (
        ('agendado', 'Agendado'),
        ('efetuado', 'Efetuado'),
        ('cancelado', 'Cancelado'),
    )

    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    observacao = models.TextField('Observação', max_length=200, null=False, default=str)
    status = models.CharField('Status', max_length=25, null=False, blank=False, choices=STATUS_CHOICES,
                              default='agendado')
    horario = models.DateTimeField('Horário')
    duracao = models.SmallIntegerField('Duração', null=False, blank=False, choices=DURACAO_CHOICES)

    def __str__(self):
        return f'{self.cliente} - {self.get_status_display()} - {self.get_duracao_display()}'
