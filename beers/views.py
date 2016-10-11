from django.views import generic

from .models import Beer, Brewery


class IndexView(generic.base.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Beer.objects.all().count()
        return context


class BeerDetailView(generic.detail.DetailView):
    model = Beer
    template_name = "beers/beer.html"


class BreweryDetailView(generic.detail.DetailView):
    model = Brewery
    template_name = "beers/brewery.html"
