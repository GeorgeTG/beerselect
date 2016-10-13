from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^beer/(?P<pk>[0-9]+)/$',
            views.BeerDetailView.as_view(),
            name='beer_detail'),
        url(r'^search/$',
            views.BeerSearchView.as_view(),
            name='beer_search'),
        url(r'^brewery/(?P<pk>[0-9]+)/$',
            views.BreweryDetailView.as_view(),
            name='brewery_detail'),
        ]
