# Generated by Django 4.1.7 on 2023-07-31 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_cancelled',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
