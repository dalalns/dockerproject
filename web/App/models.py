from django.db import models

class Courtpdfprocesstion(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    File_Name = models.CharField(max_length=400, blank=True, default='')
    Judge_Name = models.CharField(max_length=400, blank=True, default='')
    Judgement_Date = models.DateField(blank=True, null=True)
    Party_One = models.CharField(max_length=400, blank=True, default='')
    Party_Two = models.CharField(max_length=400, blank=True, default='')
    Case_Number = models.CharField(max_length=400, blank=True, default='')
    Judgement_Order =models.CharField(max_length=400, blank=True, default='')
    Judgement_Type =models.CharField(max_length=400, blank=True, default='')
    Court_Name =models.CharField(max_length=400, blank=True, default='')

    def __str__(self):
        return self.File_Name

class Requestjson(models.Model):
    Court = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.Court
    """    
    from dashboard.models import Country # imports the model
    with open('countries_continents.csv') as csvfile:
...     reader = csv.DictReader(csvfile)
...     for row in reader:
...             p = Country(country=row['Country'], continent=row['Continent'])
...             p.save()
    
    """
