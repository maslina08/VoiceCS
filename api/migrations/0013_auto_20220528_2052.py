# Generated by Django 3.2.13 on 2022-05-28 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20220528_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csat_filtred_phones',
            name='created_reason',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='csat_filtred_phones',
            name='deactivated_reason',
            field=models.TextField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
