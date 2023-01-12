from django.shortcuts import render, redirect

from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    sort_mapping = {
        "name": "name",
        "max_price": "-price",
        "min_price": "price"
    }
    if sort:
        phones = Phone.objects.order_by(sort_mapping[sort])
    else:
        phones = Phone.objects.all()
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
