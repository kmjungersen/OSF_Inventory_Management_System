#imports

import pymongo
import ast
from items import Item


class Inventory():

    def __init__(self):
        """

        :return:
        """

    def retrieve_record(self, barcode=None, item_number=None):
        """ This function will query the inventory database and then create a
        new instance of the `Item()` class for each item to enable manipulation
        of data.

        :return:
        """

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

        

    def search_records(self, query):
        """ This function queries the database using given parameters to return
        a list of records matching the query.

        :return:
        """

    def update_record(self, barcode, altered_info):
        """ This function

        :param barcode:
        :param modified_info:
        :return:
        """


if __name__ == '__main__':

    foo = Inventory()
