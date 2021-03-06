# Generated by Django 3.0.4 on 2020-03-28 01:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('joy', '0008_auto_20200328_0109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partnerimage', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.AlterModelOptions(
            name='careers',
            options={'ordering': ['pub_date']},
        ),
        migrations.AddField(
            model_name='careers',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
