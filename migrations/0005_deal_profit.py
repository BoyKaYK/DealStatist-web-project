# Generated by Django 3.2.16 on 2022-11-05 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0004_deal_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='profit',
            field=models.FloatField(default='0', verbose_name='Profit'),
        ),
    ]
