# Generated by Django 3.2 on 2021-12-02 18:49

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20)),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inside_category', to='mimar.category')),
            ],
            options={
                'verbose_name_plural': 'categories',
                'unique_together': {('slug', 'parent')},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_no', models.CharField(default='Ürün Kodu Giriniz', max_length=25)),
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
                ('seo', models.CharField(default='Seo için Bilgi Giriniz.', max_length=500)),
                ('key', models.CharField(default='Keyword için Giriş', max_length=550)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='mimar.category')),
            ],
            options={
                'ordering': ('created',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]