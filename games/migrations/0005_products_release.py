# Generated by Django 4.1.7 on 2023-03-26 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_alter_purchase_price_alter_purchase_product_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='release',
            field=models.DateField(default='2023-01-01'),
            preserve_default=False,
        ),
    ]