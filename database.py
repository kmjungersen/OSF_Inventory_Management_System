__author__ = 'kurtisjungersen'

from pymongo import MongoClient
from local import *


class Database():

    def __init__(self, debug=False):
        """ Establishes connection with MongoDB for use

        :return:
        """

        self.debugging = debug

        client = MongoClient(host=DB_NODE, port=DB_PORT)

        database = client.inventory

        if debug:

            product_collection = database.test_inventory_products
            item_collection = database.test_inventory_items

        else:

            product_collection = database.inventory_prooducts
            item_collection = database.inventory_items

        product_collection.ensure_index("product_number")
        item_collection.ensure_index("barcode_id")
        item_collection.ensure_index("item_number")

        self.db = {
            'items': item_collection,
            'products': product_collection,
        }

    def add_item(self, item):
        """ Adds a single record to the inventory database

        :param record:
        :return:
        """
        record = item.info

        return self.__write('items', record)



    def add_product(self, product):
        """ Adds a single product to the inventory database

        :param prduct:
        :return:
        """

        record = product.info

        return self.__write('products', record)

    def update_item(self, item):
        """ Updates a single item

        :param item:
        :return:
        """

        if item.is_valid:

            new_record = item.info

            self.__update('items', new_record)

    def update_product(self, product, updated_info):
        """

        :param product: an instance of the product class to be updated
        :return:
        """

        if product.is_valid:

            new_record = product.info

            self.__update('products', new_record)

    def remove_item(self, item):
        """ Removes any records that match the given query

        :param record:
        :return:
        """

        item_id = item.info.get('item_number')

        self.__remove('items', item_id)

    def find_one_item(self, query):
        """

        :param query:
        :return:
        """

        # results = self.find_items(query)
        #
        # if results.__len__() == 1:
        #
        #     return results[0]

        table = self.db.get('items')

        return table.find_one(query)

    def find_one_product(self, query):
        """

        :param query:
        :return:
        """

        results = self.find_products(query)

        if results.__len__() == 1:

            return results[0]

    def find_one(self, query, type):
        """

        :param query:
        :return:
        """

        if type == 'items':

            self.find_one_item(query)

        elif type == 'products':

            self.find_one_product(query)

    def find_items(self, query=None):
        """

        :param query:
        :return:
        """

        if not query:
            query = {}

        table = self.db.get('items')

        items = table.find(query)

        return items

    def find_products(self, query=None):
        """

        :param query:
        :return:
        """

        results = []

        return results

    def debug(self, function=None, *args):
        """

        :param function:
        :param args:
        :return:
        """

        functions = {
            'update': self.__update,
            'write': self.__write,
            'remove': self.__remove,
        }

        if self.debugging:
            func = functions.get(function)
            func(*args)

    # def write(self, record_type, record):
    #
    #     self.__write(record_type, record)

    def __update(self, record_type, new_record):
        """

        :param record:
        :param collection:
        :return:
        """

        # new_record = obj.info

        record_id_name = self.__select_record_id_name(record_type)

        record_id = new_record.get(record_id_name)

        query = {
            record_id_name: record_id,
        }

        old_record = self.find_one_item(query)

        changed_fields = set(old_record.items()) ^ set(new_record.items())

        table = self.db.get('items')

        table.update(query, {'$set': changed_fields})

    def __write(self, record_type, record):
        """

        :param record:
        :param collection:
        :return:
        """

        table = self.db.get(record_type)

        return table.insert(record)

    def __remove(self, record_type, record_id):
        """

        :param record_type:
        :param query:
        :return:
        """

        table = self.db.get(record_type)

        record_id_name = self.__select_record_id_name(record_type)

        query = {
            record_id_name: record_id,
        }

        table.remove(query)

    def __select_record_id_name(self, record_type):
        """

        :param record_type:
        :return:
        """

        record_id_name = '{record}_number'.format(
            record=record_type,
        )

        return record_id_name

