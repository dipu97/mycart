# Generated by Django 4.2.2 on 2023-06-16 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_products_delete_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]