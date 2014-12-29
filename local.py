__author__ = 'kurtisjungersen'

DB_NODE = '192.168.33.11'

DB_PORT = 8888

PRODUCT_FIELDS = [
    'item_number',
    'name',
    'quantity',
    'description',
    'notes',
    'preferred_supplier',
    'supplier_notes',
    'container_type',
    'average_cost',
]

ITEM_FIELDS = [
    'barcode_id',
    'expiration_date',
    'room',
    'unit',
    'shelf',
    'container',
    'slot_number',
    'date_added',
    'most_recently_used',
    'purchased_from',
    'cost',
]

FIELDS = [
    'barcode_id',
    'name',
    'quantity',
    'expiration_date',
    'description',
    'notes',
    'quantity',
    'container_type',
    'room',
    'unit',
    'shelf',
    'container',
    'slot_number',
    'date_added',
    'most_recently_used',
    'purchased_from',
    'cost',
    'average_cost',
    'preferred_supplier',
    'supplier_notes',
]

REQUIRED_FIELDS = [
    'barcode_id',
    'name',
    'quantity',
    'expiration_date',
]

CONTAINER_TYPES = [
    'milk_jug',
    'egg_carton',
    'box_set',
    'individual_item',
]

# DATA_TYPES = {
#     'barcode_number': 'int',
#     'item_number': 'int',
#     'manufacturer_id': 'int',
#     'quantity': 'int',
#     'container_type': 'str',
#     'room': 'str',
#     'unit': 'int',
#     'shelf': 'int',
#     'container': 'int',
#     'slot_number': 'int',
#     'description': 'str',
#     'notes': 'str',
#     'date_added': 'date',
#     'expiration_date': 'date',
#     'most_recently_used': 'date',
#     'preferred_supplier': 'str',
#     'supplier_notes': 'str',
#     'average_cost': 'float',
}