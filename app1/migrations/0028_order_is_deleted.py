# Generated by Django 4.1.7 on 2023-07-31 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0027_remove_order_date_cancelled_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]