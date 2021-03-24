from django.shortcuts import render
from .models import TravelPlan
import requests
import json
from .APITarget.APIHandler import APIHandler

# Create your views here.

def TravelPlan_display_results(request, *args, **kwargs):
    apiGetData = APIHandler("FlightPrices")
    print(apiGetData.data)
    origin=request.GET.get('origin')
    destination=request.GET.get('destination')
    obj=TravelPlan.objects.filter(origin=origin, destination=destination)
    print(origin)
    print(destination)
    context={
        'dbData':obj,
        'origin': origin,
        'destination': destination,
    }
    return render(request, "SearchResults.html",context)