from django.db import models

# Create your models here.

class Sca(models.Model):
    id = models.IntegerField(auto_created=True,serialize=False,verbose_name="ID", null=False, blank=False, default=1)
    nome = models.CharField(verbose_name= "Nome",max_length=100, null=False, blank=False)
    cpf = models.CharField(verbose_name= "CPF",max_length=11, null=False, blank=False, primary_key=True)
    matricula = models.CharField(verbose_name= "Matricula",max_length=12, null=False, blank=False)
    disciplinas = models.IntegerField(verbose_name= "Disciplinas Matriculadas", null=False, blank=False)
    curso = models.CharField(verbose_name= "Curso",max_length=100, null=False, blank=False)
