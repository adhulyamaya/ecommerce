# Generated by Django 4.1.7 on 2023-08-17 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0030_variant_image1_variants_variant_image2_variants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variant',
            name='image1_variants',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='image2_variants',
        ),
    ]
