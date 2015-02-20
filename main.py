#imports

from items import Item, Product
from database import Database
from local import *


class Inventory():

    def __init__(self):
        """

        :return:
        """

        self.db = Database()
        self.product_fields = dict(PRODUCT_FIELDS)
        self.item_fields = dict(ITEM_FIELDS)





    def duplicate(self, item_number, new_barcode):
        """ Given an item number and a new barcode number, this function will
        duplicate an entry so that the new item will have all of the metadata
        from the previous item

        :param barcode:
        :return:
        """

    def new_record(self, data):
        """ This function goes through the process of creating a new record
        and storing it in the inventory database.

        :param data:
        :return:
        """

        item = Item(data)

        if item.is_valid:

            self.db.add_item(item)

        else:

            pass

    def search_records(self, query, type):
        """ This function queries the database using given parameters to return
        a list of records matching the query.

        :return:
        """

        actual_query = {
            'collection': type,
        }

        for field, value in query.items():

            if field in self.product_fields:

                if value:

                        actual_query[field] = value

        results = self.__retrieve_records(query)

        return results

    def update_product(self, barcode, altered_info):
        """ This function

        :param barcode:
        :param modified_info:
        :return:
        """

        query = {
            'barcode_id': barcode,
        }
        products = self.__retrieve_products(query)

        cleared_to_write = True

        for product in products:

            if not product.update(altered_info):

                cleared_to_write = False

        if cleared_to_write:

            self.__write_products(products)


    def update_item(self, barcode, item_number, altered_info):
        """

        :param barcode:
        :param item_number:
        :param altered_info:
        :return:
        """

        query = {
            'barcode_id': barcode,
            'item_number': item_number,
        }

        items = self.__retrieve_items(query)

        cleared_to_write = True

        for item in items:

            if not item.update(altered_info):

                cleared_to_write = False

        if cleared_to_write:

            self.__write_items(items)





    # def __update_record(self, barcode, item_number=None):
    #     """
    #
    #     :param barcode:
    #     :param item_number:
    #     :return:
    #     """

    def __retrieve_products(self, query):
        """

        :param query:
        :return:
        """
        query['collection'] = 'products'

        records = self.__retrieve_records(query)

        products = []

        for product_info in records:

            obj = Product(product_info)

            products.append(obj)

        return products

    def __retrieve_items(self, query):
        """

        :param query:
        :return:
        """

        query['collection'] = 'items'

        records = self.__retrieve_records(query)

        items = []

        for item_info in records:

            obj = Item(item_info)

            items.append(obj)

        return items

    def __retrieve_records(self, query):
        """

        :return:
        """

        collection = query.get('collection')

        if collection:

            query.__delitem__('collection')

        records = self.db.find(query, collection=collection)

        return records

    def __write_items(self, items):
        """

        :param items:
        :return:
        """

    def __write_products(self, products):
        """

        :param products:
        :return:
        """

    def __write_records(self, records):
        """

        :param records:
        :return:
        """


if __name__ == '__main__':

    foo = Inventory()
