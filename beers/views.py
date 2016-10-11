import random

from django.http import Http404
from django.shortcuts import redirect
from django.views import generic
from django.core.urlresolvers import reverse

from .models import Beer, Brewery, BeerStyle


class IndexView(generic.base.TemplateView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        beers = Beer.objects.filter(
                style__id=int(request.POST.get('style_id')))
        try:
            beer = random.choice(beers)
        except IndexError:
            raise Http404("No beers in this category")
        return redirect(reverse('beer_detail', kwargs={'pk': beer.id}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['beers_count'] = Beer.objects.all().count()
        context['breweries_count'] = Brewery.objects.all().count()
        nonzero = list()
        for style in BeerStyle.objects.all():
            if style.beer_set.count() > 0:
                nonzero.append(style)
        context['styles'] = nonzero

        return context


class BeerDetailView(generic.detail.DetailView):
    model = Beer
    template_name = "beers/beer.html"


class BreweryDetailView(generic.detail.DetailView):
    model = Brewery
    template_name = "beers/brewery.html"


class BeerSearchView(generic.list.ListView):

    model = Beer
    template_name = "beers/search.html"

    def get_queryset(self):
        query = self.request.GET.get('query')
        return Beer.objects.filter(name__icontains=query)

