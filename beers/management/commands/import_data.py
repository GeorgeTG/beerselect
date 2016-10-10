import csv
from pathlib import Path

from django.core.management.base import BaseCommand
from beers.models import Beer, BeerCategory, BeerStyle, Brewery


class Command(BaseCommand):
    help = 'Import csv data'

    def add_arguments(self, parser):
        parser.add_argument('csv_directory', nargs=1, type=str)

    def handle(self, *args, **options):
        csv_path = Path(options['csv_directory'][0])
        # categories
        BeerCategory.objects.all().delete()
        self.stdout.write('Importing categories...')
        with (csv_path / 'categories.csv').open('r') as f:
            cat_reader = csv.DictReader(f, delimiter=',', quotechar='"')
            for row in cat_reader:
                category = BeerCategory()
                category.id = int(row['id'])
                category.name = row['cat_name']
                category.save()

        BeerStyle.objects.all().delete()
        # styles
        self.stdout.write('Importing styles...')
        with (csv_path / 'styles.csv').open('r') as f:
            style_reader = csv.DictReader(f, delimiter=',', quotechar='"')
            for row in style_reader:
                style = BeerStyle()
                category = BeerCategory.objects.get(id=row['cat_id'])
                style.id = int(row['id'])
                style.name = row['style_name']
                style.category = category
                style.save()

        Brewery.objects.all().delete()
        self.stdout.write('Importing breweries...')
        with (csv_path / 'breweries.csv').open('r') as f:
            brewery_reader = csv.DictReader(f, delimiter=',', quotechar='"')
            for row in brewery_reader:
                brewery = Brewery()
                brewery.id = int(row['id'])
                brewery.name = row['name']
                brewery.address = row['address1']
                brewery.city = row['city']
                brewery.state = row['state']
                brewery.code = row['code']
                brewery.country = row['country']
                brewery.phone = row['phone']
                brewery.website = row['website']
                brewery.description = row['descript']
                brewery.save()

        Beer.objects.all().delete()
        self.stdout.write('Importing beers...')
        with (csv_path / 'beers.csv').open('r') as f:
            beer_reader = csv.DictReader(f, delimiter=',', quotechar='"')
            for row in beer_reader:
                try:
                    beer = Beer()
                    beer.id = int(row['id'])
                    brewery = Brewery.objects.get(id=int(row['brewery_id']))
                    beer.brewery = brewery
                    beer.name = row['name']
                    beer.abv = float(row['abv'])
                    beer.ibu = float(row['ibu'])
                    beer.srm = float(row['srm'])
                    beer.upc = int(row['upc'])
                    beer.description = row['descript']
                    beer.save()
                except:
                    # just ignore errors, the database is huge anyway
                    continue
