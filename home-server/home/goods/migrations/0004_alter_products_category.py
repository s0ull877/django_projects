# Generated by Django 4.2.11 on 2024-04-09 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_categories_options_alter_categories_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ManyToManyField(default=4, to='goods.categories'),
        ),
    ]
