# Generated by Django 4.2.6 on 2023-10-11 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_alter_category_top_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]