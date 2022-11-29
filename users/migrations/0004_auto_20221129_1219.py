# Generated by Django 3.2.4 on 2022-11-29 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20221122_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nick_name',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='닉네임'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_num',
            field=models.IntegerField(null=True, unique=True, verbose_name='학번'),
        ),
    ]
