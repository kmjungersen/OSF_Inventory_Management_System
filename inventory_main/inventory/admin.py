from django.contrib import admin
from inventory.models import Product, Item
# Register your models here.


class ItemsInLine(admin.TabularInline):
    model = Item
    extra = 1


class ProductAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name']}),
        ('Product details', {
            'fields': ['barcode_id', 'product_number']
        }),

        ('Date Information', {
            'fields': ['date_first_added'],
            # 'classes': ['collapse']
        })
    ]

    inlines = [ItemsInLine]
    search_fields = ['name', 'barcode_id', 'product_number']



class ItemAdmin(admin.ModelAdmin):

    list_display = ('item_number', 'expiration_date')




admin.site.register(Product, ProductAdmin)
admin.site.register(Item, ItemAdmin)

admin.AdminSite.site_header = 'INVENTORY!!!!!  YEAH!!'