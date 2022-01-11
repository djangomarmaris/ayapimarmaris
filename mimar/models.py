from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.




class Comment(models.Model):
    info = models.TextField(max_length=500,default='Yorum giriniz.')
    name = models.CharField(max_length=20, db_index=True)


    def __str__(self):
        return self.name



class About(models.Model):
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    finish = models.CharField(max_length=20, db_index=True)
    contunie = models.CharField(max_length=20, db_index=True)
    bathroom = models.CharField(max_length=20, db_index=True)
    info = RichTextUploadingField(blank=True)



    def __str__(self):
        return self.info


class Category(models.Model):
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    parent = models.ForeignKey('self',blank=True,null=True,related_name='inside_category',on_delete=models.CASCADE)
    name = models.CharField(max_length=20, db_index=True)
    sold = models.BooleanField(default=True)
    slug = models.SlugField(max_length=20, db_index=True, unique=True)

    class Meta:
        unique_together =('slug','parent')
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name



    def get_absolute_url(self):
        return reverse('mimar:product_list_by_show', args=[self.slug])




class Sales(models.Model):
    product = models.ForeignKey(Category, related_name='House', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image4 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image5 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image6 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    name = models.CharField(max_length=200, db_index=True)
    list_info = RichTextUploadingField(blank=True)


    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete = models.CASCADE)
    product_no = models.CharField(max_length=25,default='Ürün Kodu Giriniz')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image4 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image5 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image6 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image7 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image8 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image9 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    image10 = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    description = RichTextUploadingField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    sold = models.BooleanField(default=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    seo = models.CharField(max_length=500,default="Seo için Bilgi Giriniz.")
    key = models.CharField(max_length=550,default="Keyword için Giriş")


    class Meta:
        ordering = ('created',)
        index_together = (('id', 'slug',))

    def __str__(self):
        return self.name



    def get_absolute_url(self):
        return reverse('mimar:product_detail', args=[self.id, self.slug])



class Service(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    picture = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    info = RichTextUploadingField(blank=True)



    def __str__(self):
        return self.name



class Slider(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    small = models.CharField(max_length=200, db_index=True)
    big = models.CharField(max_length=200, db_index=True)
    link = models.CharField(max_length=200, db_index=True)



    def __str__(self):
        return self.name



class Personel(models.Model):
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    name = models.CharField(max_length=200, db_index=True)
    position = models.CharField(max_length=200, db_index=True)
    facebook = models.CharField(max_length=200, db_index=True)
    instagram = models.CharField(max_length=200, db_index=True)


    def __str__(self):
        return self.name


