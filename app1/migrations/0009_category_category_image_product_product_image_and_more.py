# Generated by Django 4.1.7 on 2023-06-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_rename_category_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default='default_image.jpg', upload_to='category'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='default_image.jpg', upload_to='products'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
