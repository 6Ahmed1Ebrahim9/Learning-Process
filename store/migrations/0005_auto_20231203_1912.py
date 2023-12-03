# Generated by Django 4.2.7 on 2023-12-03 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_address_zip'),
    ]

    operations = [
        migrations.RunSQL(
            """
            INSERT INTO store_collection (title)
            VALUES ('collection1')
            """,
            """
            DELETE FROM store_collection 
            WHERE title = 'collection1';
            """
        )
    ]