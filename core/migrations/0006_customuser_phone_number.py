# Generated by Django 4.2.5 on 2023-09-29 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default=9179646209, max_length=255),
            preserve_default=False,
        ),
    ]