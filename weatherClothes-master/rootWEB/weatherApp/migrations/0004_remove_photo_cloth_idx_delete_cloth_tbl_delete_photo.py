# Generated by Django 4.1.7 on 2023-04-15 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherApp', '0003_remove_cloth_tbl_photo_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='cloth_idx',
        ),
        migrations.DeleteModel(
            name='cloth_tbl',
        ),
        migrations.DeleteModel(
            name='photo',
        ),
    ]
