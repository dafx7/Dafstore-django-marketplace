# Generated by Django 4.2.1 on 2023-07-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_rename_image_itemimage_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimage',
            name='images',
            field=models.FileField(upload_to='item_images'),
        ),
    ]