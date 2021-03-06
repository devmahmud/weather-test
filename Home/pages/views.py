from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def openMainPage(request, *args, **kwargs):
    return render(request,"TravellyHomePage.html",{})