# Generated by Django 2.1.1 on 2018-09-28 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='nome')),
            ],
            options={
                'verbose_name': 'Professor',
            },
        ),
        migrations.AlterModelOptions(
            name='situation',
            options={'verbose_name': 'Situação'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Aluno'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Disciplina'},
        ),
        migrations.RemoveField(
            model_name='subject',
            name='credits',
        ),
        migrations.AddField(
            model_name='subject',
            name='credit',
            field=models.IntegerField(default=4, verbose_name='creditos'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id_subscription',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='matricula'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=55, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='student',
            name='subject',
            field=models.ManyToManyField(related_name='rel_student', to='api.Subject'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='hours',
            field=models.IntegerField(verbose_name='horas'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=40, verbose_name='nome'),
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ManyToManyField(to='api.Teacher'),
        ),
    ]
