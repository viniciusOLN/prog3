# Generated by Django 3.2.9 on 2022-02-25 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20220225_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.company', verbose_name='Companhia'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='last_update',
            field=models.DateTimeField(default='', help_text='Última atualização sobre o produto no estoque', verbose_name='Última Atualização'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='product_in_stock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.product', verbose_name='Produto em estoque'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(default=0, help_text='Quantidade do produto no estoque', verbose_name='Quantidade'),
        ),
    ]