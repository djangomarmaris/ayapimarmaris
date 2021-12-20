from django.shortcuts import render, get_object_or_404 , redirect
from django.conf import settings
from django.core.mail import send_mail
from mimar.models import Product, Category, About, Comment, Service


def index(request):
    service = Service.objects.all()
    comment = Comment.objects.all()
    all = Category.objects.all()
    return render(request,'central/index.html',{'all':all,'comment':comment,'service':service})



def projects(request):
    products = Category.objects.all()

    return render(request,'central/projects.html',{'products':products})


def about(request):
    comment = Comment.objects.all()
    about = About.objects.all()
    return render(request,'central/about.html',{'about':about,'comment':comment})



def news(request):

    return render(request,'central/news.html')


def contact(request):
    if 'btnSubmit' in request.POST:
        if True:

            name = request.POST.get('name')
            email = request.POST.get('email')
            info = request.POST.get('info')

            subject = 'Costumer Contact Messages'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,"djangomarmaris@gmail.com"]
            contact_message = "Name:%s\nEmail:%s\nInfo:%s" % (
                name,
                email,
            info)
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
        return redirect('/')
    return render(request,'central/contact.html')




def Show(request, category_slug = None):

    products = Product.objects.filter(available=True).order_by('-id')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,'central/show.html',{'category':category,'products':products})



def product_detail(request,id, slug):

    product = get_object_or_404(Product, id = id , slug=slug, available=True)


    return render(request,'central/detail.html',{'product':product})








