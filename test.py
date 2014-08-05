from main import Inventory


class TestForProperEntryValidation():

    def __init__(self):

        self.test_dict = {
            'item_number': 12345,
            'barcode_number': 67890,
            'description': 'some really cool super awesome thing',
            'foo': 'bar',
            'room': 'that room across the hall',
            'baz': 45,

        }

        self.inventory = Inventory()

    def test_check_for_valid_fields(self):

        status, invalid_fields = self.inventory.check_for_valid_fields(self.test_dict)

        assert status == False