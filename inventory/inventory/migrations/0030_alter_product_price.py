# Generated by Django 3.2.9 on 2022-02-26 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0029_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=8, verbose_name='Preço do produto'),
        ),
    ]