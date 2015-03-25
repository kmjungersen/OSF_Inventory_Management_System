from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime
from inventory.utils import query_upc_database

from inventory.models import Product, Item


import ipdb

# Create your views here.

def index(request):
    latest_product_list = Product.objects.all()

    return render(request, 'inventory/products.html', {
        'products': latest_product_list,
    })


def add_product_form(request, error_message=None):

    return render(request, 'inventory/add_product.html', {
        'first_pass': True,
        'error_messsage': error_message,
    })

def add_product_form_from_item(request):

    return redirect('add_product_form')


def add_product(request):
    # ipdb.set_trace()

    p = Product(
        name=request.POST['product_name'],
        barcode_id=request.POST['barcode_id']
    )

    p.save()

    return redirect('index')


def lookup_product(request, form_origin):

    barcode_id = request.POST['barcode_id']

    if barcode_id == '':

        return redirect('add_product_form')

    template = 'inventory/add_{origin}.html'.format(
        origin=form_origin,
    )

    product_found = False
    product_name = ''
    description = ''
    # error_message = ''

    try:
        product = Product.objects.get(barcode_id__exact=barcode_id)

        product_found = True
        product_name = product.name
        description = product.description

    except Exception:

        if form_origin == 'product':

            data = query_upc_database(barcode_id)

            if data:

                # ipdb.set_trace()

                # TODO return a selection of possible items and an "is this your item?" dialogue
                # TODO fix pyscan to be better

                # product_found = True

                product_name = data[0].get('productname')
                # description = data[0].get('description')

    return render(request, template, {
        'first_pass': False,
        'product_found': product_found,
        'barcode_id': barcode_id,
        'product_name': product_name,
        'description': description,
        # 'error_message': error_message,
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

    expiration_date = datetime.strptime(expiration_date_str, '%Y-%m-%d')

    product = Product.objects.get(barcode_id__exact=barcode_id)

    item = Item(
        product=product,
        lot_number=lot_number,
        cost=cost,
        expiration_date=expiration_date,
    )

    item.save()

    return redirect('index')


def home(request):

    return redirect('index')


def view_product(request, barcode_id):

    product = Product.objects.get(barcode_id__exact=barcode_id)

    return render(request, 'inventory/view_product.html', {
        'product': product,
    })


