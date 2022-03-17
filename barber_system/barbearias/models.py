from django.db import models


# Create your models here.

class Barbearia(models.Model):
    razao_social = models.CharField('Razão Social', max_length=100, blank=False, null=False)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=100, blank=False, null=False)
    cnpj = models.CharField('CNPJ', max_length=14, blank=False, null=False)
    email = models.CharField('E-mail', max_length=100, blank=True)
    horario_atendimento = models.TextField('Horário de atendimento', blank=True)
    facebook = models.URLField('Facebok', max_length=200, blank=True)
    twitter = models.URLField('Twitter', max_length=200, blank=True)
    instagram = models.URLField('Instagram', max_length=200, blank=True)
    youtube = models.URLField('YouTube', max_length=200, blank=True)
    telefone = models.CharField('Telefone', max_length=32, blank=True)
    celular = models.CharField('Celular', max_length=32, blank=True)
    logo = models.ImageField('Logo', upload_to='images')

    def __str__(self):
        return self.razao_social

    class Meta:
        verbose_name = 'Barbearia'
        verbose_name_plural = 'Barbearias'
        ordering = ['razao_social']


class CortesCabelo(models.Model):
    CORTES_CHOICES = (
        ('baixo', 'Baixo'),
        ('medio', 'Médio'),
        ('alto', 'Alto'),
        ('baixo_degrade', 'Baixo degrade'),
        ('media_degrade', 'Médio degrade'),
        ('alto_degrade', 'Alto degrade'),
    )

    modelo = models.CharField('Modelo', max_length=50, null=False, choices=CORTES_CHOICES)
    preco = models.FloatField('Preço', null=False)
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE)
    foto = models.ImageField('Foto', upload_to='images')

    def __str__(self):
        return self.modelo
