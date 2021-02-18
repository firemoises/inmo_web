from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
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


    """
    #prueba333
    def perfil(request,agente_id):

    agent = Agent.objects.get(id=agente_id)
    inmuebles = Inmueble.objects.get(agente=agent.id,estado=1) #Inmueble.objects.all().filter(id=portfolio_id)
   
    return render(request,"core/perfil.html",{"inmuebles":inmuebles,"agent":agent})
    """