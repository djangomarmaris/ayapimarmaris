from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views




app_name = 'mimar'


urlpatterns =[
    path('',views.index,name ='index'),
    path('projects/',views.projects,name='projects'),
    path('about/',views.about,name='about'),
    path('news/',views.news,name='news'),
    path('contact/',views.contact,name='contact'),
    path('<int:id>/<str:slug>/', views.product_detail, name = 'product_detail'),
    path('<str:category_slug>/', views.Show, name='product_list_by_show'),


]


