# Generated by Django 4.2.5 on 2023-09-27 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Customeraddress', serialize=False, to='store.customer'),
        ),
    ]