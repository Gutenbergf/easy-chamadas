# Generated by Django 2.1.2 on 2018-11-16 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20181111_0421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testeusuario',
            name='user',
        ),
    ]
