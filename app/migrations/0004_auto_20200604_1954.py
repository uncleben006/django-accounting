# Generated by Django 3.0.6 on 2020-06-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200604_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.CharField(default='ben_wang', max_length=64),
        ),
        migrations.AddField(
            model_name='record',
            name='user',
            field=models.CharField(default='ben_wang', max_length=64),
        ),
    ]