# Generated by Django 3.0.4 on 2020-03-28 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joy', '0009_auto_20200328_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='partners',
            name='name',
            field=models.CharField(default=True, max_length=30),
        ),
    ]
