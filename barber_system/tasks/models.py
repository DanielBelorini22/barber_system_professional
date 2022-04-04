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
