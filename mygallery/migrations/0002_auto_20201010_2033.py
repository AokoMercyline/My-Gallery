# Generated by Django 3.1.2 on 2020-10-10 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Images',
            },
        ),
        migrations.AlterModelOptions(
            name='image',
            options={},
        ),
    ]
