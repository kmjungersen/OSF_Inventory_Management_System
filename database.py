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

        self.collection = self.db.inventory

        self.collection.ensure_index("barcode_number")

    def add(self, record):
        """ Adds a single record to the inventory database

        :param record:
        :return:
        """

        self.collection.insert(record)

    def remove(self, remove_query):
        """ Removes any records that match the given query

        :param record:
        :return:
        """

        self.collection.remove(remove_query)

    def find(self, query):
        """ Uses a query to find records

        :param query:
        :return:
        """

        results = self.collection.find(query)

        return results
