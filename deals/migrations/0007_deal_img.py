# Generated by Django 3.2.16 on 2022-11-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0006_profit'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='img',
            field=models.TextField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/2048px-No_image_available.svg.png', verbose_name='item_src'),
        ),
    ]
