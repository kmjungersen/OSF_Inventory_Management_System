from django.conf.urls import patterns, url

from inventory import views
#
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'add_product_form/$', views.add_product_form),
    url(r'add_item_form/$', views.add_item_form),

    url(r'add_product/$', views.add_product, name='add_product'),
    url(r'add_item/$', views.add_item, name='add_item'),

    url(r'(?P<form_origin>\w+)/lookup_product/$', views.lookup_product, name='lookup_product')
)