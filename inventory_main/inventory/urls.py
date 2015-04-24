from django.conf.urls import patterns, url

from inventory import views
#
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    # url(r'add_product_form/$', views.add_product_form, name='add_product_form'),
    url(r'add_item_form/$', views.add_item_form),

    url(r'view_product/(?P<barcode_id>\w+)/$', views.view_product, name='view_product'),
    url(r'view_product/(?P<barcode_id>\w+)/add_item/$', views.add_item_from_product),
    url(r'view_product/(?P<barcode_id>\w+)/(?P<item_id>\w+)/$', views.view_item),


    url(r'view_item/(?P<barcode_id>\w+)/(?P<item_id>\w+)/$', views.view_item, name='view_item'),
    url(r'view_checked_out_items/$', views.view_checked_out_items, name='checked_out_items'),

    url(r'view_item/(?P<barcode_id>\w+)/(?P<item_id>\w+)/(?P<action>\w+)/$', views.checkout_form, name='checkout_form'),
    url(r'view_item/(?P<barcode_id>\w+)/(?P<item_id>\w+)/(?P<action>\w+)/go/$', views.checkout, name='checkout'),

    url(r'add_product/$', views.add_product_form, name='add_product_initial'),
    url(r'add_product/lookup/$', views.add_product_form, name='add_product_lookup'),
    url(r'add_product/(?P<barcode_id>\w+)/$', views.add_product_form, name='add_product_form'),
    url(r'add_product/(?P<barcode_id>\w+)/go/$', views.add_product, name='add_product'),


    url(r'add_item/$', views.add_item_form, name='add_item_initial'),
    url(r'add_item/lookup/$', views.add_item_form, name='add_item_lookup'),
    url(r'add_item/(?P<barcode_id>\w+)/$', views.add_item_form, name='add_item_form'),
    url(r'add_item/(?P<barcode_id>\w+)/go/$', views.add_item, name='add_item'),

    url(r'add_location/(?P<location_type>\w+)/$', views.add_location_form, name='add_location_initial')

    # url(r'(?P<form_origin>\w+)/lookup_product/$', views.lookup_product, name='lookup_product'),




)
