# Generated by Django 3.1.1 on 2021-02-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0024_auto_20201223_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='reg',
            field=models.URLField(blank=True),
        ),
    ]