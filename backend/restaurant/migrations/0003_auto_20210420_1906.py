# Generated by Django 3.1.3 on 2021-04-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20210420_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=5, null=True, verbose_name='Сумма за весь заказ'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=5, null=True, verbose_name='Общая стоимость'),
        ),
    ]
