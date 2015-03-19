from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime

from inventory.models import Product, Item


import ipdb

# Create your views here.

def index(request):
    latest_product_list = Product.objects.all()

    return render(request, 'inventory/products.html', {'products': latest_product_list})


def add_product_form(request):

    return render(request, 'inventory/add_product.html', {'first_pass': True})


def add_product(request):
    ipdb.set_trace()

    p = Product(
        name=request.POST['name'],
        barcode_id=request.POST['barcode_id']
    )

    p.save()

    return redirect('index')


def lookup_product(request, form_origin):

    barcode_id = request.POST['barcode_id']

    template = 'inventory/add_{origin}.html'.format(
        origin=form_origin,
    )

    try:
        product = Product.objects.get(barcode_id__exact=barcode_id)

        return render(request, template, {
            'first_pass': False,
            'product_found': True,
            'barcode_id': product.barcode_id,
            'product_name': product.name,
            'description': product.description,
        })

    except Exception as error_message:

        return render(request, template, {
            'first_pass': False,
            'product_found': False,
            'barcode_id': barcode_id,
            'error_message': error_message,
        })


def add_item_form(request):

    # if request.POST.get('product_found'):
    #
    #     print('foooo')

    return render(request, 'inventory/add_item.html', {
        'first_pass': True,
    })


def add_item(request):

    barcode_id = request.POST.get('barcode_id')
    lot_number = request.POST.get('lot_number')
    cost = request.POST.get('cost')
    expiration_date_str = str(request.POST.get('expiration_date'))
    # datetime_str = '{date} {time}'.format(
    #     date=expiration_date_str,
    #     time=
    # )
    #
    expiration_date = datetime.strptime(expiration_date_str, '%Y-%m-%d')
    # time = datetime.time()
    #
    #
    # expiration_date = datetime.combine(expiration_date, time)

    # expiration_date = timezone.datetime(expiration_date_str)

    product = Product.objects.get(barcode_id__exact=barcode_id)

    item = Item(
        product=product,
        lot_number=lot_number,
        cost=cost,
        expiration_date=expiration_date,
    )

    item.save()

    return redirect('index')