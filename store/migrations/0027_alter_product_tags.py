# Generated by Django 4.2.6 on 2023-10-11 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_alter_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.CharField(blank=True, choices=[('Newest', 'Newest'), ('Best Seller', 'Best Seller'), ('Most Visited', 'Most Visited'), ('Highest Quality', 'Highest Quality')], default='', max_length=50, null=True),
        ),
    ]
