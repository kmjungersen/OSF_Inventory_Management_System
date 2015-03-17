from django.contrib import admin
from inventory.models import Product, Item
# Register your models here.


class ItemsInLine(admin.TabularInline):
    model = Item
    extra = 1


class ProductAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name']}),
        ('Date Information', {
            'fields': ['date_first_added'],
            'classes': ['collapse']
        })
    ]
    inlines = [ItemsInLine]

admin.site.register(Product, ProductAdmin)
admin.site.register(Item)

admin.AdminSite.site_header = 'INVENTORY!!!!!  YEAH!!'