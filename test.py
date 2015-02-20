from items import Item, Product
from pymongo import MongoClient
from local import *


class TestDB():

    def __init__(self):
        c = MongoClient(host=DB_NODE, port=DB_PORT)
        db = c.inventory
        self.items = db.items
        self.products = db.products

class TestItems:

    def setup(self):

        self.test_item_info = {
            'barcode_id': 12345,
            'expiration_date': '1/23/15',
            'room': '5',
            'unit': '6',
            'shelf': '2',
            'date_added': '1/15/15',
            'most_recently_used': '1/20/15',
            'purchased_from': 'ACME inc',
            'cost': '350',
            'item_number': 78465,
            'checked_in': True,
        }

        return self.test_item_info

    def setup_item(self, info=None):

        if not info:
            info = self.test_item_info

        item = Item(info)

        return item

    def test_item_fields(self):

        i = self.setup_item()

        assert i.info == self.test_item_info

    def test_required_fields(self):

        i = self.setup_item()

        assert i.is_valid

    def test_required_fields_missing(self):

        info = self.test_item_info
        info.__delitem__('barcode_id')

        i = self.setup_item(info)

        assert not i.is_valid


class TestProducts:

    def setup(self):

        self.test_item_info = {
            'barcode_id': 12345,
            'expiration_date': '1/23/15',
            'room': '5',
            'unit': '6',
            'shelf': '2',
            'date_added': '1/15/15',
            'most_recently_used': '1/20/15',
            'purchased_from': 'ACME inc',
            'cost': '350',
            'item_number': 78465,
            'checked_in': True,
        }

        test_items = []
        self.number_of_items = 5

        for x in range(0, self.number_of_items):

            self.test_item_info['barcode_id'] = x
            item = Item(self.test_item_info)

            test_items.append(item)

        self.test_product_info = {
            'product_number': 1235456,
            'name': 'foo product',
            'items': test_items,
            'description': 'foooooo',
            'notes': 'here are some cool notes',
            'preferred_supplier': 'ACME',
            'supplier_notes': 'beep beep',
            'container_type': 'milk_jug',
            'average_cost': 4562,
        }

    def setup_product(self, info=None):

        if not info:
            info = self.test_product_info

        product = Product(info)

        return product

    def test_product_fields(self):

        p = self.setup_product()

        assert p.info == self.test_product_info

    def test_required_fields(self):

        p = self.setup_product()

        assert p.is_valid

    def test_required_fields_missing(self):

        info = self.test_product_info
        info.__delitem__('average_cost')

        p = self.setup_product(info)

        assert not p.is_valid

    def test_product_count(self):

        p = self.setup_product()

        assert p.quantity == self.number_of_items


