from django.contrib.auth.models import User, Group
from rest_framework import serializers
from inventory.models import Item, LocationRoom, LocationUnit, LocationShelf


class ItemSerializer(serializers.ModelSerializer):
    """
    foo
    """

    class Meta:
        model = Item
        # fields = (
        #     'product',
        #     'checked_in',
        #     'cost',
        #     'lot_number',
        # )


class LocationRoomSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = LocationRoom


class LocationUnitSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = LocationUnit


class LocationShelfSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = LocationShelf

#
# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')