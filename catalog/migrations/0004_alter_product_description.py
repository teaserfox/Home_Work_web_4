# Generated by Django 4.2.3 on 2023-07-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_rename_picture_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=80, null=True, verbose_name='Описание'),
        ),
    ]