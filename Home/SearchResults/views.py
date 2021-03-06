from django.shortcuts import render
from .models import TravelPlan
# Create your views here.

def TravelPlan_display_results(request, *args, **kwargs):
    obj=TravelPlan.objects.all
    origin=request.GET.get('origin')
    destination=request.GET.get('destination')
    print(origin)
    print(destination)
    context={
        'dbData':obj,
        'origin': origin,
        'destination': destination,
    }
    return render(request, "dispTravelsData.html",context)