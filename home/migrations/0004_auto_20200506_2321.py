# Generated by Django 3.0.5 on 2020-05-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200506_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumb',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]
