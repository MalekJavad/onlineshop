# Generated by Django 4.1 on 2022-10-01 11:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]