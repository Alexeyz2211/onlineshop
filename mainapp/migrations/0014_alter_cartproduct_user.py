# Generated by Django 3.2.4 on 2021-11-18 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_order_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.customer', verbose_name='Покупатель'),
        ),
    ]
