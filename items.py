"""

"""

class Item():

    def __init__(self):

        pass




class Product():

    def __init__(self, record_info):

        self.info = record_info

        self.is_valid = self.validate()

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

    def checkout(self, barcode):
        """ This function checks out an item given a barcode number

        :param barcode:
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