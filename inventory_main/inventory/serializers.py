from django.contrib.auth.models import User, Group
from rest_framework import serializers
from inventory.models import Item, LocationRoom


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


class LocationSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = LocationRoom

#
# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')