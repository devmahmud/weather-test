from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class TravelPlan(models.Model):
    travelID     = models.PositiveIntegerField(unique=True, default=0, editable=False)
    origin       = models.CharField(max_length=50)
    destination  = models.CharField(max_length=50)
    price        = models.DecimalField(max_digits=6, decimal_places=2)
    travelOrigins =  ArrayField(models.CharField(max_length=100),default=list)
    travelDestination =  ArrayField(models.CharField(max_length=100),default=list)
