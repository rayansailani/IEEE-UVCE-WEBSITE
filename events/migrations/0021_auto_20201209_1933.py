# Generated by Django 3.1.1 on 2020-12-09 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_auto_20201209_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(max_length=100),
        ),
    ]
