from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Beer


def index(request):
    total = Beer.objects.all().count()
    return render(request, 'beers/index.html', {'total': total})


def beer_detail(request, beer_id):
    response = 'Beer id: %s' % beer_id
    return HttpResponse(response)
