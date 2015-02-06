from main import Inventory


# class TestForProperEntryValidation():
#
#     def __init__(self):
#
#         self.test_dict = {
#             'item_number': 12345,
#             'barcode_number': 67890,
#             'description': 'some really cool super awesome thing',
#             'foo': 'bar',
#             'room': 'that room across the hall',
#             'baz': 45,
#
#         }
#
#         self.inventory = Inventory()
#
#     def test_check_for_valid_fields(self):
#
#         status, invalid_fields = self.inventory.check_for_valid_fields(self.test_dict)
#
#         assert status == False


foo = Inventory()from items import Item, Product


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
