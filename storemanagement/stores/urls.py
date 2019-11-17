from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns=[

	url(r'^$', index, name='index'),

	url(r'^display_product$', display_product, name='display_product'),

	url(r'^add_product$', add_product, name='add_product'),

	url(r'^edit_product/(?P<pk>\d+)$', edit_product, name='edit_product'),

	url(r'^sell_product/(?P<pk>\d+)$', sell_product, name='sell_product'),

	url(r'^delete_product/(?P<pk>\d+)$', delete_product, name='delete_product'),

	url(r'^get_stock$', get_stock, name='get_stock'),

    path('search/', SearchResultsView.as_view(), name='search_results'),

    path('', HomePageView.as_view(), name='index'),


]