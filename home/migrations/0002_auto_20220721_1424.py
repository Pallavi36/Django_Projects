# Generated by Django 3.0 on 2022-07-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joined',
            name='dues',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
