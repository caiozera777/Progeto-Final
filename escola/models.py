from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def _str_(self):
        return f'{self.nome}'   

class Curso(models.Model):
    nivel = (
    ('B', 'Basico'),
    ('I', 'Intermediario'),
    ('A', 'Avancado')
    )

    codigo_curso = models.CharField(max_length=9)
    descricao = models.CharField(max_length=11)
    nivel = models.CharField(max_length=1, choices = nivel, blank = False , null = False)


    def _str_(self):
        return f'{self.descricao}'