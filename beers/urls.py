from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('beer/<int:pk>/', views.BeerDetailView.as_view(), name='beer_detail'),
    path('search/', views.BeerSearchView.as_view(), name='beer_search'),
    path('brewery/<int:pk>/', views.BreweryDetailView.as_view(), name='brewery_detail'),
]
