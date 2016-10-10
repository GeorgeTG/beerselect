from django.contrib import admin

from .models import BeerCategory, BeerStyle, Brewery, Beer

admin.site.register(BeerCategory)
admin.site.register(BeerStyle)
admin.site.register(Brewery)
admin.site.register(Beer)
