# Generated by Django 3.1.5 on 2021-05-24 10:20

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0002_auto_20210523_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='my_field',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('item_key1', 'Item title 1.1'), ('item_key2', 'Item title 1.2'), ('item_key3', 'Item title 1.3'), ('item_key4', 'Item title 1.4'), ('item_key5', 'Item title 1.5')], max_length=49, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='my_field2',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Item title 2.1'), (2, 'Item title 2.2'), (3, 'Item title 2.3'), (4, 'Item title 2.4'), (5, 'Item title 2.5')], max_length=3, null=True),
        ),
    ]
