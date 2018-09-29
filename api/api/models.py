from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(verbose_name='nome', max_length=55)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'


class Subject(models.Model):
    name = models.CharField(max_length=40, verbose_name='nome')
    hours = models.IntegerField(verbose_name='horas')
    credit = models.IntegerField(verbose_name='creditos', default=4)
    teacher = models.ManyToManyField('Teacher')

    class Meta:
        verbose_name = 'Disciplina'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=55, verbose_name='nome')
    id_subscription = models.IntegerField(primary_key=True, verbose_name='matricula')
    subject = models.ManyToManyField(Subject, related_name='rel_student')

    class Meta:
        verbose_name = 'Aluno'

    def __str__(self):
        return self.name

class Situation(models.Model):
    SITUACAO = (
    ('REP', 'Reprovado por falta'),
    ('ATV', 'Ativo'),
    )
    sit = models.CharField(max_length=30, choices=SITUACAO, default='ATV')

    class Meta:
        verbose_name = 'Situação'

class Faul(models.Model):
    fauts = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)