# Generated by Django 5.0.7 on 2024-11-02 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_alter_products_name_products_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ManyToManyField(to='products.category'),
        ),
    ]