from django.shortcuts import render
from .models import TravelPlan
# Create your views here.

def TravelPlan_display_results(request, *args, **kwargs):
    obj=TravelPlan.objects.all
    context={
        'dbData':obj,
        #'origin':obj.origin,
        #'destination': obj.destination,
        #'price': obj.price,
        "arrays": [[399, "london"], [233, "manchester"], [233, "lisboa"], [233, "liverpool"]],
    }

    return render(request, "dispTravelsData.html",context)