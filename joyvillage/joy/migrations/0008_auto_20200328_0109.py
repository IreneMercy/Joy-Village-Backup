# Generated by Django 3.0.4 on 2020-03-28 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joy', '0007_auto_20200327_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('requirements', models.CharField(max_length=255)),
                ('instruction', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
