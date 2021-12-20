from django.contrib import admin
from .models import Category, Product, About, Comment , Service


# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','parent','name','slug','sold']
    list_editable = [ 'sold']
    prepopulated_fields = {'slug':('name',)}




class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','category','price','available','created','updated','sold']
    list_filter = ['available','created','updated','category']
    list_editable = ['price','available','sold']
    prepopulated_fields = {'slug':('name',)}



class AboutAdmin(admin.ModelAdmin):
    list_display = ['id']



class CommentAdmin(admin.ModelAdmin):
    list_display = ['name']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Service,ServiceAdmin)


admin.site.site_header = 'İGD Effect'