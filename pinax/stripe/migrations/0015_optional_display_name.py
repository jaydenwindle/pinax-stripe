# Generated by Django 2.0.2 on 2018-04-05 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_stripe', '0013_charge_outcome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='display_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]