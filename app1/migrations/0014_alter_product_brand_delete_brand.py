# Generated by Django 4.1.7 on 2023-07-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_brand_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]