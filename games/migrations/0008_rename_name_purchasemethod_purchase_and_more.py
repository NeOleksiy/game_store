# Generated by Django 4.1.7 on 2023-03-11 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_remove_products_purchase_method_name_purchasemethod'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='name_purchaseMethod',
            new_name='purchase',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='purchase_method',
            new_name='purchaseMethod',
        ),
        migrations.AddField(
            model_name='products',
            name='purchaseMethod',
            field=models.ManyToManyField(through='games.purchase', to='games.purchasemethod'),
        ),
    ]
