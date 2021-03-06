from django.db import models

# Create your models here.
class TravelPlan(models.Model):
    destination  = models.CharField(max_length=50)
    origin       = models.CharField(max_length=50)
    price        = models.DecimalField(max_digits=6, decimal_places=2)