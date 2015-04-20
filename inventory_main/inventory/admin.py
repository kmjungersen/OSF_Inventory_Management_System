from django.contrib import admin
from inventory.models import Product, Item, LocationRoom, LocationUnit, LocationShelf
# Register your models here.


class ItemsInLine(admin.TabularInline):
    model = Item
    extra = 0


class ProductAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name']}),
        ('Product details', {
            'fields': ['barcode_id', 'description', 'notes']
        }),

        ('Date Information', {
            'fields': ['date_first_added'],
            # 'classes': ['collapse']
        })
    ]

    inlines = [ItemsInLine]
    search_fields = [
        'name',
        'barcode_id',
        'product_number',
    ]

    list_display = ('name', 'barcode_id', 'quantity', 'items_checked_out')


class ItemAdmin(admin.ModelAdmin):

    list_display = ('product', 'lot_number', 'expiration_date')

    fieldsets = [
        (None, {'fields': ['product', 'checked_in']}),
        ('Item Details', {
            'fields': ['lot_number', 'cost']
        }),
        ('Location Information', {
            'fields': ['location_room', 'location_unit', 'location_shelf']
        })
    ]


class RoomAdmin(admin.ModelAdmin):

    list_display = ('location_id', 'name')


class UnitAdmin(admin.ModelAdmin):

    list_display = ('location_id', 'room', 'type', 'temperature')


admin.site.register(LocationUnit, UnitAdmin)

admin.site.register(LocationRoom, RoomAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Item, ItemAdmin)

admin.AdminSite.site_header = 'INVENTORY!!!!!  YEAH!!'