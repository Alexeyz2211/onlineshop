# Generated by Django 3.2.4 on 2021-07-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20210709_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='related_cart', to='mainapp.CartProduct'),
        ),
    ]
