# Generated by Django 3.1.1 on 2020-10-05 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20201005_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='approved_by',
            field=models.CharField(blank=True, default=None, max_length=40, null=True),
        ),
    ]
