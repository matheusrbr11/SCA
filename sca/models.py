from django.db import models

# Create your models here.

class Sca(models.Model):
    nome = models.CharField(verbose_name= "Nome",max_length=100, null=False, blank=False)
    cpf = models.CharField(verbose_name= "CPF",max_length=11, null=False, blank=False)
    matricula = models.CharField(verbose_name= "Matricula",max_length=12, null=False, blank=False)
    curso = models.CharField(verbose_name= "Curso",max_length=100, null=False, blank=False)
