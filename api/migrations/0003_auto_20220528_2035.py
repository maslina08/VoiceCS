# Generated by Django 3.2.13 on 2022-05-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220528_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='csat_filtred_phones',
            name='created_reason',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='csat_filtred_phones',
            name='deactivated_reason',
            field=models.TextField(default='', max_length=255),
        ),
    ]