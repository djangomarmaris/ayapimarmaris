# Generated by Django 3.2 on 2021-12-11 16:24

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mimar', '0005_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('image2', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('image3', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('image4', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('image5', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('info', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
            ],
        ),
    ]
