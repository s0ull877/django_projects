# Generated by Django 4.2.11 on 2024-04-09 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_alter_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ManyToManyField(default=[4], to='goods.categories'),
        ),
    ]