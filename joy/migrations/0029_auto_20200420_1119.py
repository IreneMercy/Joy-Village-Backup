# Generated by Django 2.2.10 on 2020-04-20 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joy', '0028_auto_20200420_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='newsimage',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
