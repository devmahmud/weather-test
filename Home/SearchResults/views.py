from django.shortcuts import render
from .models import TravelPlan
import requests
import json
from .APITarget.APIHandler import APIHandler
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def TravelPlan_display_results(request, *args, **kwargs):
    origin=request.GET.get('origin')
    destination=request.GET.get('destination')
    print("orig ", origin)
    print("dest ", destination)
    api_Handler_data = APIHandler("FlightPrices").data
    #print(json.loads(api_Handler_data))
    apiGetData = json.loads(api_Handler_data)
    for i in apiGetData:
        print(i['id'])
        travels_origins = []
        travels_destinations = []
        itinerary = i['itineraries']
        for k in itinerary:
            print("kkkkkkkk", k, "kkkkkkkk")
            segments = k['segments']
            for travels in segments:
                print("departure: ", travels['departure']['iataCode'])
                travels_origins.append( travels['departure']['iataCode'])
                print("arrival: ", travels['arrival']['iataCode'])
                travels_destinations.append(travels['arrival']['iataCode'])
        if TravelPlan.objects.filter(travelID=i['id']).exists():
            TravelPlan.objects.filter(travelID=i['id']).update(origin=origin,destination=destination,price=55,travelOrigins=travels_origins , travelDestination=travels_destinations)
            print("replace")
        else:
            add_TravelPlan = TravelPlan(travelID=i['id'],origin=origin,destination=destination,price=55,travelOrigins=travels_origins , travelDestination=travels_destinations)
            print("new")
            add_TravelPlan.save()
        print("-------------------------------\n")
    obj=TravelPlan.objects.filter(origin=origin, destination=destination)
    for values in obj:
        all_origins = values.travelOrigins
        all_destinations = values.travelDestination
        for o in all_origins:
            print("origin:", o)
        for d in all_destinations:
            print("destination:", d)
    print(destination)
    context={
        'dbData':obj,
        'origin': origin,
        'destination': destination,
    }
    return render(request, "SearchResults.html",context)