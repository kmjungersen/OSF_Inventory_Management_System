from django.conf.urls import patterns, url

from inventory import views
#
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/add_product/$', views.add_product, name='add_product')
)