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

    #TODO add decorators
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

    def checkout(self):
        """ This function checks out an item given a barcode number

        :param barcode:
        :return:
        """

        return self.__item_checking('out')

    def checkin(self):
        """

        :return:
        """

        return self.__item_checking('in')

    def __item_checking(self, in_or_out):
        """ Helper method to handle all checking in or out of items.

        :return:
        """

        checked_in = self.info['checked_in']

        if checked_in and in_or_out == 'in':

            msg = 'Error!  Item already checked in!'

            return msg

        elif not checked_in and in_or_out == 'out':

            msg = 'Error!  Item already checked out!'

            return msg

        elif (checked_in and in_or_out == 'in') or \
                (not checked_in and in_or_out == 'out'):

            self.info['checked_in'] = False

            msg = 'Item number {numb} has been checked {in_or_out}'.format(
                numb=self.info['item_number'],
                in_or_out=in_or_out,
            )

            return msg

        else:

            msg = 'Error! Unhandled exception in __item_checking()!'

            return msg


class Product():

    def __init__(self, record_info):
        """

        :param record_info:
        :return:
        """

        self.items = []
        self.info = record_info

        self.quantity = self.__update_quantity()

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

        required_fields = dict(PRODUCT_FIELDS)

        for field, required in required_fields.items():

            if required and not info.get(field):

                is_valid = False

        self.is_valid = is_valid

        return is_valid

    def update(self, updated_info):
        """ This function will update any data that has changed since the
        record was pulled and then log those changes

        :param updated_info:
        :return:
        """
        info = self.info

        for key, value in updated_info.items():

            info[key] = value

        if self.validate(info=info):

            self.info = info

            msg = 'Item updated successfully!'

            return msg

        else:

            msg = 'Error! Some items to update were not valid!'

            return msg

    def __update_quantity(self):
        """ This function updates the quantity based on the number of items
        is has associated with it.

        :return:
        """

        quantity = 0

        for item in self.info['items']:

            quantity += 1

        self.quantity = quantity
        self.info['quantity'] = self.quantity

        return quantity

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