"""

"""

from database import Database
from local import *


class Item():

    def __init__(self, info):
        """

        :return:
        """

        self.info = info

        # self.db = Database()
        self.is_valid = False
        self.validate()

    def validate(self, info=None):
        """ Validates the required information fields for an item exist before
        it can be recorded.

        :return:
        """

        if not info:

            info = self.info

        is_valid = True

        required_fields = dict(ITEM_FIELDS)

        for field, required in required_fields.items():

            if required and not info.get(field):
                print(field)

                is_valid = False

        self.is_valid = is_valid

        return is_valid

    def update(self, updated_info):
        """ Updates an item with new information

        :param updated_info:
        :return:
        """

        updated = False

        info = self.info

        for key, value in updated_info.items():

            info[key] = value

        if self.validate(info=info):

            self.info = info

            updated = True

            msg = 'Item updated successfully!'

        else:

            msg = 'Error! Some items to update were not valid!'

        return updated, msg
        """ This function checks out an item given a barcode number

        :param barcode:
        :return:
        """



class Product():

    def __init__(self, record_info):
        """

        :param record_info:
        :return:
        """

        self.items = []
        self.info = {}

        self.db = Database()

        self.is_valid = self.validate()

    def fetch_data(self):
        """

        :return:
        """

        self.info = self.db.find()

    def validate(self):
        """ This function validates the data given for the item and will
        identify and return any validation errors

        :return:
        """
        valid = True

        return valid


    def update(self, updated_info):
        """ This function will update any data that has changed since the
        record was pulled and then log those changes

        :param updated_info:
        :return:
        """





    #TODO - this should be done using decorators so that every single change
    # is logged
def log_change(self, updated_info):
        """ This function will log any updates for a record so they can be
        retrieved later if needed.  This allows monitoring of stock levels
        for automatic threshold adjustment.

        :return:
        """


# class Kit():
#
#     def __init__(self):
#
#         pass
#
#
# class VialPack():
#
#     def __init__(self):
#
#         pass
#
#
# class StandaloneItem():
#
#     def __init__(self):
#
#         pass