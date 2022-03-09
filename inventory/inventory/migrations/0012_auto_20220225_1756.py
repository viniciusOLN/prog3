# Generated by Django 3.2.9 on 2022-02-25 20:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='mail',
            field=models.CharField(default='', help_text='Email da companhia', max_length=50, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.CharField(default='', help_text='Nome da companhia', max_length=80, verbose_name='Nome da companhia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(default='', help_text='Telefone da companhia', max_length=11, verbose_name='Telefone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='site',
            field=models.CharField(default='', help_text='Site da companhia', max_length=100, verbose_name='Site'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='last_update',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Última atualização sobre o produto no estoque'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='product_in_stock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.company'),
        ),
        migrations.AddField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(default=0, help_text='Quantidade do produto no estoque'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Identificador Único para a companhia', primary_key=True, serialize=False),
        ),
    ]