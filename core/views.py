from django.shortcuts import render,HttpResponse
from portfolio.models import Inmueble
from agents.models import Agent

# Create your views here.
def home(request):
    return render(request,"core/index.html")

def portfolio(request,portfolio_id):
    inmueble = Inmueble.objects.get(id=portfolio_id) #Inmueble.objects.all().filter(id=portfolio_id)
    agent = Agent.objects.get(id=inmueble.agente_id)
    return render(request,"core/index.html",{"inmueble":inmueble,"agent":agent})

