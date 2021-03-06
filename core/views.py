from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render,HttpResponse,redirect
from core.scraper import scrape_data_corotos
from django.template import RequestContext
from django.core.mail import EmailMessage
from portfolio.models import Inmueble
from contact.forms import ContactForm
from django.conf.urls import handler404, handler500
from django.urls import reverse
from agents.models import Agent
import os

# Create your views here.
def home(request):
    return render(request,"core/index.html")

def portfolio(request,portfolio_id): 

    inmueble = Inmueble.objects.get(id=portfolio_id) #Inmueble.objects.all().filter(id=portfolio_id)
    agent = Agent.objects.get(id=inmueble.agente_id)
    contact_form = ContactForm()

    ### Formulario
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST) #Si el formulario fue enviado lo llenamos

        if contact_form.is_valid():
            nombre = request.POST.get("nombre",'')
            telefono = request.POST.get("telefono",'')
            correo = request.POST.get("correo",'')
            mensaje = request.POST.get("mensaje",'')

            #Enviamos el correo
            asunto = f"Nuevo mensaje desde asenfi-inmo.com de {nombre}"
            cuerpo = f"{mensaje} Escrito por:\n\nNombre: {nombre}\nTelefono: {telefono}\nCorreo: {correo}"
            correo_origen = "info@asenfi-inmo.com"

            if agent.correo2:
                correo_destino = [agent.correo,agent.correo2]
            else:
                correo_destino = [agent.correo]
                
            correo_reply = [correo]
            email_del_cliente = EmailMessage(asunto,cuerpo,correo_origen,correo_destino,correo_reply)

            try:
                email_del_cliente.send()
                #Si todo salio bien enviamos un mensaje
                return redirect(f'/portfolio/{portfolio_id}/?ok')
            except:
                #Si algo salio mal
                return redirect(f'/portfolio/{portfolio_id}/?fail')

    if inmueble.estado == 1:
        return render(request,"core/index.html",{"inmueble":inmueble,"agent":agent,"form":contact_form})


def agents(request,agents_id):
        agent = Agent.objects.get(id=agents_id)
        inmuebles = Inmueble.objects.filter(agente=agent.id,estado=1) #Inmueble.objects.all().filter(id=portfolio_id)
        inmueblesGral = Inmueble.objects.filter(estado=1) #Inmueble.objects.all().filter(id=portfolio_id)
        contador  =  inmuebles.all().count()
        contGral  =  inmueblesGral.all().count()
        return render(request,"core/agents.html",{"inmuebles":inmuebles,"agent":agent, "contador":contador,"inmueblesGral":inmueblesGral,"contGral":contGral})


#404: página no encontrada
def pag_404_not_found(request, exception):
  from django.shortcuts import render
  return render(request,'core/404.html')

#500: error en el servidor
def error_500_view(request):
    return render(request,'core/500.html')
 

def prueba(request):

    #url = "https://www.corotos.com.do/sc/inmuebles-en-venta/casas"
    url = "https://www.corotos.com.do/sc/inmuebles-en-venta/apartamentos"
    tipo_neg = "Venta"
    #driver = os.getcwd()+"/chromedriver_88.exe"
    driver = os.getcwd()+"/geckodriver.exe"
    solo_agentes = 0
    no_dupli = 1
    resp = os.getcwd()

    #Vamos a llamar esto n veces teniendo en cuenta que siempre se para solo
    for n in range(1):
        feats = scrape_data_corotos(url,tipo_neg,2,driver,loads=0,solo_agentes=solo_agentes,no_dupli=no_dupli)

    return render(request,"core/prueba.html",{"resp":feats})

def prueba2(request):
    from pyvirtualdisplay import Display

    with Display():

        #url = "https://www.corotos.com.do/sc/inmuebles-en-venta/casas"
        url = "https://www.corotos.com.do/sc/inmuebles-en-venta/apartamentos"
        tipo_neg = "Venta"
        #driver = os.getcwd()+"/chromedriver_88.exe"
        driver = os.getcwd()+"/geckodriver.exe"
        solo_agentes = 0
        no_dupli = 1
        resp = os.getcwd()

        #Vamos a llamar esto n veces teniendo en cuenta que siempre se para solo
        for n in range(1):
            feats = scrape_data_corotos(url,tipo_neg,2,driver,loads=0,solo_agentes=solo_agentes,no_dupli=no_dupli)

    return render(request,"core/prueba.html",{"resp":feats})
            