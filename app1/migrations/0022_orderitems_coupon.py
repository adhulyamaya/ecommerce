# Generated by Django 4.1.7 on 2023-07-21 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_remove_order_coupon_cart_discount_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.coupon'),
        ),
    ]