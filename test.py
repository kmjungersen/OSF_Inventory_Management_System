from items import Item, Product


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

        for x in range[5]:

            self.test_item_info['barcode_id'] = x
            item = Item(self.test_item_info)

            test_items.append(item)

        self.test_product_info = {
            'product_number': 1235456,
            'name': 'foo product',
            'quantity': 45,
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
        info.__delitem__('barcode_id')

        p = self.setup_product(info)

        assert not p.is_valid


