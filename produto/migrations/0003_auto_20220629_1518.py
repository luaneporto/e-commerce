# Generated by Django 3.1.14 on 2022-06-29 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_alter_produto_preco_marketing_variacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='variacao',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
