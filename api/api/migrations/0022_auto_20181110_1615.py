# Generated by Django 2.1.2 on 2018-11-10 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_testeusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='name',
            field=models.CharField(max_length=55, verbose_name='Nome da turma'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='students',
            field=models.ManyToManyField(to='api.Student', verbose_name='Estudantes'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Teacher', verbose_name='Professor'),
        ),
    ]
