# Generated by Django 2.0.7 on 2018-07-31 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reward', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='end_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='reward',
            name='start_time',
            field=models.CharField(max_length=100),
        ),
    ]
