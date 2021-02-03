from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from portfolio.models import Inmueble
from agents.models import Agent
from contact.forms import ContactForm

# Create your views here.
def home(request):
    return render(request,"core/index.html")

def portfolio(request,portfolio_id):

    inmueble = Inmueble.objects.get(id=portfolio_id) #Inmueble.objects.all().filter(id=portfolio_id)
    agent = Agent.objects.get(id=inmueble.agente_id)
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST) #Si el formulario fue enviado lo llenamos

        if contact_form.is_valid():
            nombre = request.POST.get("nombre",'')
            telefono = request.POST.get("telefono",'')
            correo = request.POST.get("correo",'')
            mensaje = request.POST.get("mensaje",'')
            #Si todo salio bien enviamos un mensaje
            return redirect(f'/portfolio/{portfolio_id}/?ok')

    return render(request,"core/index.html",{"inmueble":inmueble,"agent":agent,"form":contact_form})

