# Generated by Django 3.2 on 2022-01-11 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mimar', '0004_sales_list_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='image2',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='sales',
            name='image3',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='sales',
            name='image4',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='sales',
            name='image5',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='sales',
            name='image6',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='sales',
            name='image7',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='sales',
            name='image8',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d'),
        ),
    ]
