# Generated by Django 2.2.10 on 2020-04-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joy', '0025_kiambu_donate'),
    ]

    operations = [
        migrations.AddField(
            model_name='muranga',
            name='donate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nairobi',
            name='donate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nakuru',
            name='donate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nyeri',
            name='donate',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
