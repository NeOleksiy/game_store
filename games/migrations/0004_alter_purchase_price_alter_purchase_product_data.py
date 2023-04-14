# Generated by Django 4.1.7 on 2023-03-25 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_remove_products_account_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product_data',
            field=models.CharField(max_length=80),
        ),
    ]
