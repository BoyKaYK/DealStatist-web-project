# Generated by Django 3.2.16 on 2022-11-01 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='item_name',
            field=models.CharField(max_length=100, verbose_name='Item Name'),
        ),
    ]