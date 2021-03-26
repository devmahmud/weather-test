from django.shortcuts import render
from .models import TravelPlan
import requests
import json
from .APITarget.APIHandler import APIHandler

# Create your views here.

def TravelPlan_display_results(request, *args, **kwargs):
    #apiGetData = APIHandler("FlightPrices")
    origin=request.GET.get('origin')
    destination=request.GET.get('destination')
    if origin == "ola":
        origin = "BHX"
        print("orig ", origin)
    if destination == "that":
        destination = "OPO"
        print("dest ",destination)
    apiGetData = json.loads(APIHandler("FlightPrices",origin=origin,destination=destination).data)

    for i in apiGetData:
        print("-------------------------------\n")
        print("hellooo", i['id'], "hellooo \n")
        itinerary = i['itineraries']
        for k in itinerary:
            print ("kkkkkkkk",k,"kkkkkkkk")
            segments = k['segments']
            for travels in segments:
                print("departure: ", travels['departure']['iataCode'])
                print("arrival: ", travels['arrival']['iataCode'])
       #print("hellooo", i['arrival'], "hellooo \n")
        print("-------------------------------\n")
    obj=TravelPlan.objects.filter(origin=origin, destination=destination)
    print(origin)
    print(destination)
    context={
        'dbData':obj,
        'origin': origin,
        'destination': destination,
    }
    return render(request, "SearchResults.html",context)