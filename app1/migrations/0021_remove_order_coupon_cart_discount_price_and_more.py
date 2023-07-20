# Generated by Django 4.1.7 on 2023-07-20 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_order_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='coupon',
        ),
        migrations.AddField(
            model_name='cart',
            name='discount_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]