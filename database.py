__author__ = 'kurtisjungersen'

from pymongo import MongoClient
from local import *


class Database():

    def __init__(self):
        """ Establishes connection with MongoDB for use

        :return:
        """

        self.client = MongoClient(host=DB_NODE, port=DB_PORT)

        self.db = self.client.inventory

        self.product_collection = self.db.inventory_prooducts
        self.item_collection = self.db.inventory_items

        self.product_collection.ensure_index("item_number")
        self.item_collection.ensure_index("barcode_number")

    def add_item(self, item):
        """ Adds a single record to the inventory database

        :param record:
        :return:
        """



    def add_product(self, product):
        """ Adds a single product to the inventory database

        :param prduct:
        :return:
        """

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

    def remove(self, remove_query):
        """ Removes any records that match the given query

        :param record:
        :return:
        """


    def find(self, query, collection):
        """ Uses a query to find records

        :param query:
        :param collection:
        :return:
        """

        if not collection:

            collection = 'all'


        results = []


        return results
        