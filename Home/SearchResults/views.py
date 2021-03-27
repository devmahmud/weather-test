from django.shortcuts import render
from .models import TravelPlan
import requests
import json
from .APITarget.APIHandler import APIHandler
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def TravelPlan_display_results(request, *args, **kwargs):
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')
    print("orig ", origin)
    print("dest ", destination)
    api_Handler_data = APIHandler("FlightPrices", origin=origin, destination=destination).data
    # print(json.loads(api_Handler_data))
    apiGetData = json.loads(api_Handler_data)
    for i in apiGetData:
        print(i['id'])
        standard_price = i['price']['grandTotal']
        travels_origins = []
        travels_destinations = []
        itinerary = i['itineraries'][0]
        segments = itinerary['segments']
        for travels in segments:
            print("departure: ", travels['departure']['iataCode'])
            travels_origins.append(travels['departure']['iataCode'])
            print("arrival: ", travels['arrival']['iataCode'])
            travels_destinations.append(travels['arrival']['iataCode'])
        if TravelPlan.objects.filter(travelID=i['id']).exists():
            TravelPlan.objects.filter(travelID=i['id']).delete()
        add_TravelPlan = TravelPlan(travelID=i['id'], origin=origin, destination=destination, price=standard_price,
                                    travelOrigins=travels_origins, travelDestination=travels_destinations)
        add_TravelPlan.save()
        print("-------------------------------\n")
    obj = TravelPlan.objects.filter(origin=origin, destination=destination)

    for values in obj:
        all_origins = values.travelOrigins
        all_destinations = values.travelDestination
        print("----------------showing values from itinerary--------------\n")
        for o in all_origins:
            print("origin:", o)
        for d in all_destinations:
            print("destination:", d)
        print("----------------showing values from itinerary--------------\n")
    context = {
        'dbData': obj,
        'origin': origin,
        'destination': destination,
    }
    return render(request, "SearchResults.html", context)
