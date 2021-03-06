# Generated by Django 3.2 on 2022-01-07 18:41

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('image2', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('image3', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('finish', models.CharField(db_index=True, max_length=20)),
                ('contunie', models.CharField(db_index=True, max_length=20)),
                ('bathroom', models.CharField(db_index=True, max_length=20)),
                ('info', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('name', models.CharField(db_index=True, max_length=20)),
                ('sold', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inside_category', to='mimar.category')),
            ],
            options={
                'verbose_name_plural': 'categories',
                'unique_together': {('slug', 'parent')},
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(default='Yorum giriniz.', max_length=500)),
                ('name', models.CharField(db_index=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Personel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('position', models.CharField(db_index=True, max_length=200)),
                ('facebook', models.CharField(db_index=True, max_length=200)),
                ('instagram', models.CharField(db_index=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('picture', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('info', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('small', models.CharField(db_index=True, max_length=200)),
                ('big', models.CharField(db_index=True, max_length=200)),
                ('link', models.CharField(db_index=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='House', to='mimar.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_no', models.CharField(default='??r??n Kodu Giriniz', max_length=25)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('image2', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('image3', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('image4', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('image5', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('image6', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('image7', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('image8', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('image9', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('image10', models.ImageField(blank=True, upload_to='products/%y/%m/%d')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('sold', models.BooleanField(default=True)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('seo', models.CharField(default='Seo i??in Bilgi Giriniz.', max_length=500)),
                ('key', models.CharField(default='Keyword i??in Giri??', max_length=550)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='mimar.category')),
            ],
            options={
                'ordering': ('created',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
