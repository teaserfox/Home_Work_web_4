# Generated by Django 4.2.3 on 2023-07-18 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_delete_student_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='picture',
            new_name='image',
        ),
    ]