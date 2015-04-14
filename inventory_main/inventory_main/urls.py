from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from inventory import views

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
# router.register(r'items', views.ItemSerializer, base_name='items')
# router.register(r'groups', views.GroupSerializer, base_name='groups')

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'inventory_main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', TemplateView.as_view(template_name='index.html')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^inventory/', include('inventory.urls')),

    # API ROUTES
    url(r'^items/$', views.ItemViewSet.as_view(), name='item_list'),
    # url(r'^location/$', views.LocationViewSet.as_view(), name='location_list'),
    url(r'^location/(?P<location_type>\w+)/$', views.LocationViewSet.as_view(), name='location_list_with_type'),
    url(r'^location/(?P<location_type>\w+)/(?P<location_id>\w+)/$', views.LocationViewSet.as_view(), name='location_specific'),

    url(r'^location/(?P<location_type>\w+)/(?P<location_id>\w+)/children/$', views.LocationViewSet.as_view(), name='location_specific_with_children'),

)

urlpatterns = format_suffix_patterns(urlpatterns)
