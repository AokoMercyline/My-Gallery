# Generated by Django 3.1.2 on 2020-10-10 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery', '0005_auto_20201010_2056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='author',
            new_name='location',
        ),
    ]