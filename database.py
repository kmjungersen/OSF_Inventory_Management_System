__author__ = 'kurtisjungersen'

from pymongo import MongoClient
from local import *


class Database():

    def __init__(self):
        """ Establishes connection with MongoDB for use

        :return:
        """

        client = MongoClient(host=DB_NODE, port=DB_PORT)

        database = client.inventory

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

        self.__write(record, 'items')

    def add_product(self, product):
        """ Adds a single product to the inventory database

        :param prduct:
        :return:
        """

        record = product.info

        self.__write(record, 'products')

    def update_item(self, item, updated_info):
        """ Updates a single item

        :param item:
        :return:
        """



    def update_product(self, product, updated_info):
        """

        :param product: an instance of the product class to be updated
        :return:
        """

        product_number = product.info.get('product_number')

        query = {
            'product_number': product_number,
        }



    def remove_item(self, remove_query):
        """ Removes any records that match the given query

        :param record:
        :return:
        """

    def find_one_item(self, query):
        """

        :param query:
        :return:
        """

        results = self.find_items(query)

        if results.__len__() == 1:

            return results[0]

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

    def find_items(self, query):
        """

        :param query:
        :return:
        """

        results = []

        table = self.db.get('items')

        items = table.find(query)

        return results

    def find_products(self, query):
        """

        :param query:
        :return:
        """

        results = []

        return results

    def __update(self, record_type, new_record):
        """

        :param record:
        :param collection:
        :return:
        """

        # new_record = obj.info

        obj = '{record}_number'.format(
            record=record_type,
        )

        obj_number = new_record.get(obj)

        query = {
            obj: obj_number,
        }

        old_record = self.find_one_item(query)

        changed_fields = set(old_record.items()) ^ set(new_record.items())

        table = self.db.get('items')

        table.update(query, {'$set': changed_fields})

    def __write(self, record, collection):
        """

        :param record:
        :param collection:
        :return:
        """

        table = self.db.get(collection)

        table.insert(record)