# Generated by Django 4.2.11 on 2024-04-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_categories_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelTable(
            name='categories',
            table='category',
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('descriptiom', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods_image')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('category', models.ManyToManyField(to='goods.categories')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'product',
            },
        ),
    ]