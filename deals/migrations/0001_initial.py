# Generated by Django 3.2.16 on 2022-11-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100, verbose_name='Name')),
                ('price_buy', models.FloatField(verbose_name='Buy price')),
                ('price_sell', models.FloatField(verbose_name='Sell price')),
                ('deal_status', models.BooleanField(default='0', max_length=1, verbose_name='Deal status')),
                ('date', models.DateTimeField(verbose_name='Deal date')),
            ],
        ),
    ]
