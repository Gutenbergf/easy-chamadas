# Generated by Django 2.1.2 on 2018-11-11 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20181110_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=55, unique=True, verbose_name='nome'),
        ),
    ]