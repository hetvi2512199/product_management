# Generated by Django 4.1.1 on 2023-04-06 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_product_category_product_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='des',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]