# Generated by Django 3.2.13 on 2022-05-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20220528_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csat_filtred_phones',
            name='is_deactivated',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
