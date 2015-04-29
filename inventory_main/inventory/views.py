from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime

from inventory.utils import query_upc_database, lookup_item, lookup_product, add_location_room
from inventory.models import Product, Item, LocationRoom, LocationUnit, LocationShelf, Distributor
from inventory.local import *


import ipdb

# Create your views here.


def index(request):
    latest_product_list = Product.objects.all()

    return render(request, 'inventory/products.html', {
        'products': latest_product_list,
    })


def add_product_form(request, barcode_id=None, error_message=None):

    product_name = ''
    description = ''
    first_pass = True
    product_found = False

    if barcode_id:

        first_pass = False

        product = lookup_product(barcode_id, new_product=True)

        if product:

            if type(product) == str:

                product_name = product

            else:

                product_name = product.name
                description = product.description
                product_found = True

    else:

        barcode_id = request.POST.get('barcode_id')

        if barcode_id:

            return redirect('add_product_form', barcode_id=barcode_id)

    return render(request, 'inventory/add_product.html', {
        'first_pass': first_pass,
        'error_messsage': error_message,
        'barcode_id': barcode_id,
        'product_name': product_name,
        'description': description,
        'product_found': product_found,
    })


def add_product(request, barcode_id):
    # ipdb.set_trace()

    name = request.POST['product_name']
    description = request.POST['description']
    notes = request.POST['notes']

    p = Product(
        barcode_id=barcode_id,
        name=name,
        description=description,
        notes=notes,
    )

    p.save()

    return redirect('view_product', barcode_id=barcode_id)


def add_item_form(request, barcode_id=None, error_message=None):

    first_pass = True
    product_found = False
    product = None

    if barcode_id:

        first_pass = False

        product = lookup_product(barcode_id)

        if product:

            product_found = True

    else:

        barcode_id = request.POST.get('barcode_id')

        if barcode_id:

            return redirect('add_item_form', barcode_id=barcode_id)

    return render(request, 'inventory/add_item.html', {
        'first_pass': first_pass,
        'product_found': product_found,
        'product': product,
        'error_message': error_message,
        'default_expiration': DEFAULT_EXPIRATION,
        "barcode_id": barcode_id,
    })


def add_item(request, barcode_id):

    lot_number = request.POST.get('lot_number')
    cost = request.POST.get('cost')
    expiration_date_str = str(request.POST.get('expiration_date'))

    if expiration_date_str == '':

        expiration_date_str = '2016-4-{days}'.format(
            days=DEFAULT_EXPIRATION
        )

    expiration_date = datetime.strptime(expiration_date_str, '%Y-%m-%d')

    location_room = request.POST.get('location_room')
    location_unit = request.POST.get('location_unit')
    location_shelf = request.POST.get('location_shelf')


    product = Product.objects.get(barcode_id__exact=barcode_id)

    item = Item(
        product=product,
        lot_number=lot_number,
        cost=cost,
        expiration_date=expiration_date,
        location_room=location_room,
        location_unit=location_unit,
        location_shelf=location_shelf,
    )

    item.save()

    item_id = item.id

    return redirect('view_item', barcode_id=barcode_id, item_id=item_id)


def add_item_from_product(request, barcode_id):

    return redirect("add_item_form", barcode_id=barcode_id)


def view_product(request, barcode_id):

    product = Product.objects.get(barcode_id__exact=barcode_id)

    return render(request, 'inventory/view_product.html', {
        'product': product,
    })


def view_checked_out_items(request):

    products = Product.objects.all()

    products_with_checked_out_items = []

    for p in products:

        if p.items_checked_out >= 1:

            products_with_checked_out_items.append(p)

    return render(request, 'inventory/view_checked_out_items.html', {
        'products': products_with_checked_out_items,
    })


def view_item(request, barcode_id, item_id):

    product = Product.objects.get(barcode_id__exact=barcode_id)

    item = product.item_set.get(id__exact=item_id)

    return render(request, 'inventory/view_item.html', {
        'item': item,
    })


def checkout_form(request, barcode_id, item_id, action):

    item = lookup_item(barcode_id, item_id)

    return render(request, 'inventory/checkout_form.html', {
        'item': item,
        'checkout': action,
    })


def checkout(request, barcode_id, item_id, action):

    item = lookup_item(barcode_id, item_id)

    if action == 'checkout':

        item.checked_in = False

    elif action == 'checkin':

        item.checked_in = True

    item.save()

    return redirect('view_item', barcode_id=barcode_id, item_id=item_id)


def add_location_form(request, location_type=None, error_message=None):

    rooms = LocationRoom.objects.all()

    return render(request, 'inventory/add_location_form.html', {
        'location_type': location_type,
        'rooms': rooms,
        'error_message': error_message,
    })


def add_location(request, location_type):

    utility_switch = {
        'room': add_location_room,
    }

    utility = utility_switch.get(location_type)

    utility(request)

    return redirect('index')


def location_lookup(request, room_id=None, unit_id=None, shelf_id=None):

    if room_id:

        pass

    else:

        location_list = LocationRoom.objects.all()

    return


# from django.contrib.auth.models import User, Group
from rest_framework import generics
from inventory.serializers import ItemSerializer, LocationRoomSerializer, LocationUnitSerializer, LocationShelfSerializer


class ItemViewSet(generics.ListAPIView):
    """
    foo
    """

    model = Item
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()

        return queryset


# TODO - fix  all of this!


class LocationViewSet(generics.ListAPIView):
    """
    """
    serializers = {
        'room': LocationRoomSerializer,
        'unit': LocationUnitSerializer,
        'shelf': LocationShelfSerializer,
    }

    # model = LocationRoom

    def get_queryset(self):

        room_id = self.kwargs.get('room_id')
        unit_id = self.kwargs.get('unit_id')
        shelf_id = self.kwargs.get('shelf_id')

        location_set = []

        if unit_id:

            location_set = self.get_shelf_set(room_id, unit_id)

        elif room_id:

            location_set = self.get_unit_set(room_id)

        else:

            location_set = self.get_room_set()

        return location_set

    def get_room_set(self):

        room_set = LocationRoom.objects.all()

        return room_set

    def get_unit_set(self, room_id):

        room_set = self.get_room_set()

        for room in room_set:

            if room.room_id == room_id:

                unit_set = room.locationunit_set.all()

                return unit_set

    def get_shelf_set(self, room_id, unit_id):

        unit_set = self.get_unit_set(room_id)

        for unit in unit_set:

            if unit.unit_id == unit_id:

                shelf_set = unit.locationshelf_set.all()

                return shelf_set




        # location_type = self.kwargs.get('location_type')
        # location_id = self.kwargs.get('location_id')
        #
        # self.model = self.locations.get(location_type)
        #
        # if not self.model:
        #
        #     raise KeyError('This location type does not exist!')
        #
        # if location_id:
        #
        #     queryset = self.model.objects.filter(location_id=location_id)
        #
        # else:
        #
        #     queryset = self.model.objects.all()
        #
        # return queryset






#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     foo
#     """
#
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer