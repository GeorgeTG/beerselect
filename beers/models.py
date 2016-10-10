from django.db import models


class Brewery(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    code = models.CharField(max_length=25)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=55)
    website = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'breweries'


class BeerCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'beer categories'


class BeerStyle(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(BeerCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Beer(models.Model):
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    style = models.ForeignKey(BeerStyle, on_delete=models.CASCADE, null=True)
    abv = models.FloatField()
    ibu = models.FloatField()
    srm = models.FloatField()
    upc = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
