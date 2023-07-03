# Generated by Django 4.1.7 on 2023-07-03 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_rename_cart_variant_cart_variant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat', models.CharField(max_length=255)),
                ('locality', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('pincode', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(max_length=255)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.custom_user')),
            ],
        ),
    ]
