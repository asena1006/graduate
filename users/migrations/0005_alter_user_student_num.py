# Generated by Django 3.2.4 on 2022-12-11 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20221129_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_num',
            field=models.IntegerField(null=True, verbose_name='학번'),
        ),
    ]
