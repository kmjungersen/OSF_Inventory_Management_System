#imports

# import pymongo
import ast


class Inventory():

    def __init__(self):

        self.fields = [
            'barcode_number',
            'item_number',
            'manufacturer_id',
            'quantity',
            'container_type',
            'room',
            'unit',
            'shelf',
            'container',
            'slot_number',
            'description',
            'notes',
            'date_added',
            'expiration_date',
            'most_recently_used',
            'preferred_supplier',
            'supplier_notes',
        ]

        self.container_types = [
            'milk_jug',
            'egg_carton',
            'box_set',
            'individual_item',
        ]

        self.data_types = {
            'barcode_number': 'int',
            'item_number': 'int',
            'manufacturer_id': 'int',
            'quantity': 'int',
            'container_type': 'str',
            'room': 'str',
            'unit': 'int',
            'shelf': 'int',
            'container': 'int',
            'slot_number': 'int',
            'description': 'str',
            'notes': 'str',
            'date_added': 'date',
            'expiration_date': 'date',
            'most_recently_used': 'date',
            'preferred_supplier': 'str',
            'supplier_notes': 'str',
            'average_cost': 'float',
        }

        self.inventory_dir = 'inventory/main.db'

        self.db = []
        self.fetch_db()

    def new_record(self, new_entry):

        fields_are_valid, invalid_fields = self.check_for_valid_fields(new_entry)

        if fields_are_valid:

            # new_line = str(new_entry)

            new_line  = new_entry

            with open(self.inventory_dir, 'w+') as inventory:

                # inventory.seek(2)

                inventory.write(new_line)

            status = 'Record successfully added.'

        else:

            status = 'Invalid entry fields: {0}'.format(str(invalid_fields))

        return status

    def retrieve_records(self, user_query):

        results = self.query_selection(user_query)

        print results

    def query_selection(self, query_list):

        selection = self.fetch_db()
        results = []

        for query in query_list:

            for entry in selection:

                value = entry.get(query)

                if value:

                    if entry[query] == query_list[query]:

                        results.append(entry)

                else:

                    selection.remove(entry)

                if selection.__len__() == 0:

                    found_entry = False

                    break

        return results

    def modify_record(self):

        pass

    def log_transaction(self):

        pass

    def fetch_db(self, return_db=False):

        entries = []

        # with open(self.inventory_dir, 'r') as inventory:
        #
        #     for line in inventory:
        #
        #         line = line.replace('\n', '')
        #
        #         dict_of_line = ast.literal_eval(line)
        #
        #         entries.append(dict_of_line)

        self.db = entries

        if return_db:

            return entries


    def check_for_valid_fields(self, entry):

        status = True
        invalid_fields = []

        for field in entry:

            if field not in self.fields:

                status = False
                invalid_fields.append(field)

        return status, invalid_fields

if __name__ == '__main__':

    foo = Inventory()

    some_dict = {
        'shelf': 5467,
        'room': 'foo',
        # 'foo': 'bar',
        # 'baz': 'asdfa',
    }

    print foo.new_record(some_dict)





























