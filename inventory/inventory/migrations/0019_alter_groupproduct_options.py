# Generated by Django 3.2.9 on 2022-02-25 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_auto_20220225_1817'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupproduct',
            options={'verbose_name': 'Produto em Estoque', 'verbose_name_plural': 'Produtos em Estoque'},
        ),
    ]