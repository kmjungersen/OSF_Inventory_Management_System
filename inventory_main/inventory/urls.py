from django.conf.urls import patterns, url

from inventory import views
#
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'add_product_form/$', views.add_product_form, name='add_product_form'),
    url(r'add_product_form/P?<error_message>/$', views.add_product_form, name='add_product_form_error'),

    url(r'add_item_form/$', views.add_item_form),

    url(r'add_product/$', views.add_product, name='add_product'),
    url(r'add_item/$', views.add_item, name='add_item'),

    url(r'(?P<form_origin>\w+)/lookup_product/$', views.lookup_product, name='lookup_product'),

    url(r'home/$', views.home, name='home'),

    url(r'view_product/(?P<barcode_id>\w+)/$', views.view_product, name='view_product'),
    url(r'add_product_form/from_item/$', views.add_product_form_from_item)
)