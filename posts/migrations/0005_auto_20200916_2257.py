# Generated by Django 3.1.1 on 2020-09-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200916_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Poster',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
