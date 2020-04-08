# Generated by Django 2.2.10 on 2020-04-03 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joy', '0023_auto_20200403_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10)),
                ('venue', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=155)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'PastEvents',
                'ordering': ['pub_date'],
            },
        ),
        migrations.AlterModelOptions(
            name='events',
            options={'ordering': ['pub_date'], 'verbose_name_plural': 'UpcomingEvents'},
        ),
    ]