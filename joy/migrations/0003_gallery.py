# Generated by Django 3.0 on 2020-03-21 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joy', '0002_auto_20200318_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagefield', models.ImageField(upload_to='media/')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
