# Generated by Django 3.1.1 on 2020-09-17 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200917_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_sig_head',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='membership_no',
            field=models.CharField(blank=True, default=' ', max_length=8, unique=True),
        ),
    ]
