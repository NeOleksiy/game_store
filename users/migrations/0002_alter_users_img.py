# Generated by Django 4.1.7 on 2023-03-18 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='users_img'),
        ),
    ]