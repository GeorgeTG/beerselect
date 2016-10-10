from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^(?P<beer_id>[0-9]+)/$', views.beer_detail, name='beer_detail'),
        ]
