# Generated by Django 3.1.5 on 2021-01-24 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_item_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemImages',
            new_name='ItemImage',
        ),
    ]