# Generated by Django 4.1.7 on 2023-03-24 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='purchaseMethod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.purchasemethod'),
        ),
    ]
