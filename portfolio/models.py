from django.db import models
from agents.models import Agent

# Create your models here.
class Inmueble(models.Model):
    titulo = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    zona = models.CharField(max_length=100)
    prox = models.CharField(max_length=200,verbose_name="Proximo a")
    moneda_choices = ( ('P', 'Pesos'), ('D', 'Dolares'),)
    moneda = models.CharField(max_length=1,default='P', choices=moneda_choices)

    tipo_inmo_choices = ( (1, 'Apartamento'), (2, 'Casa'), (3, 'Local'), (4, 'Solar'), (5, 'Edificio'))
    tipo_inmo = models.IntegerField(default=1, choices=tipo_inmo_choices,verbose_name="Planta electrica")

    habs = models.PositiveSmallIntegerField(verbose_name="Habitaciones")
    banos = models.PositiveSmallIntegerField(verbose_name="Baños")
    mts = models.FloatField(verbose_name="Metraje")
    parqueos = models.PositiveSmallIntegerField(verbose_name="Parqueos")
    parqueos_techados = models.BooleanField()
    piso = models.PositiveSmallIntegerField(verbose_name="Piso")
    sala = models.BooleanField()
    comedor = models.BooleanField()
    balcon = models.BooleanField()
    terraza = models.BooleanField()

    planta_choices = ( (0, 'Sin planta'), (1, 'Planta full'), (2, 'Planta solo areas comunes'))
    planta = models.IntegerField(default=0, choices=planta_choices,verbose_name="Planta electrica")

    gas_choices = ( (0, 'Sin gas comun'), (1, 'Gas comun sin medidor'), (2, 'Gas comun con medidor'))
    gas = models.IntegerField(default=0, choices=gas_choices,verbose_name="Gas comun")

    ascensor = models.BooleanField()

    seguridad24 = models.BooleanField(verbose_name="Seguridad 24 horas")
    piscina = models.BooleanField()
    gym = models.BooleanField()
    area_comun = models.BooleanField(verbose_name="Area comun")
    salon_actividades = models.BooleanField(verbose_name="Salon de actividades")
    area_inf = models.BooleanField(verbose_name="Area infantil")
    sauna = models.BooleanField()
    mant = models.IntegerField(verbose_name="Cuota de mantenimiento",blank=True)

    desc = models.TextField(verbose_name="Descripcion",blank=True)

    image1 = models.ImageField(verbose_name="Imagen 1", upload_to="Inmuebles", blank=True)
    image2 = models.ImageField(verbose_name="Imagen 2", upload_to="Inmuebles", blank=True)
    image3 = models.ImageField(verbose_name="Imagen 3", upload_to="Inmuebles", blank=True)
    image4 = models.ImageField(verbose_name="Imagen 4", upload_to="Inmuebles", blank=True)
    image5 = models.ImageField(verbose_name="Imagen 5", upload_to="Inmuebles", blank=True)
    image6 = models.ImageField(verbose_name="Imagen 6", upload_to="Inmuebles", blank=True)
    image7 = models.ImageField(verbose_name="Imagen 7", upload_to="Inmuebles", blank=True)
    image8 = models.ImageField(verbose_name="Imagen 8", upload_to="Inmuebles", blank=True)
    image9 = models.ImageField(verbose_name="Imagen 9", upload_to="Inmuebles", blank=True)
    image10 = models.ImageField(verbose_name="Imagen 10", upload_to="Inmuebles", blank=True)

    image_condo = models.ImageField(verbose_name="Imagen del condominio (horizontal)", upload_to="Inmuebles")

    dest1 = models.CharField(max_length=200,blank=True,default="Localizada en el corazon de la ciudad")
    dest2 = models.CharField(max_length=200,blank=True,default="2 pisos de parqueo")
    dest3 = models.CharField(max_length=200,blank=True,default="Estructura resistente a terremotos")
    dest4 = models.CharField(max_length=200,blank=True,default="Extinguidores en cada piso")
    dest5 = models.CharField(max_length=200,blank=True,default="Cerco electrico en las areas comunes")
    dest6 = models.CharField(max_length=200,blank=True)
    dest7 = models.CharField(max_length=200,blank=True)
    dest8 = models.CharField(max_length=200,blank=True)
    dest9 = models.CharField(max_length=200,blank=True)
    dest10 = models.CharField(max_length=200,blank=True)
    dest11 = models.CharField(max_length=200,blank=True)
    dest12 = models.CharField(max_length=200,blank=True)

    cerc1 = models.CharField(max_length=200,blank=True,default="A x minutos del supermercado x")
    cerc2 = models.CharField(max_length=200,blank=True,default="A x minutos del metro x")
    cerc3 = models.CharField(max_length=200,blank=True,default="A x calles del mcdonald's de la avenida x")
    cerc4 = models.CharField(max_length=200,blank=True,default="A x calles de la clinica x")
    cerc5 = models.CharField(max_length=200,blank=True)
    cerc6 = models.CharField(max_length=200,blank=True)
    cerc7 = models.CharField(max_length=200,blank=True)
    cerc8 = models.CharField(max_length=200,blank=True)
    cerc9 = models.CharField(max_length=200,blank=True)
    cerc10 = models.CharField(max_length=200,blank=True)
    cerc11 = models.CharField(max_length=200,blank=True)
    cerc12 = models.CharField(max_length=200,blank=True)

    map = models.TextField(verbose_name="Link de la zona")


    agente = models.ForeignKey(Agent, verbose_name="Agente", on_delete=models.PROTECT) #PROTECT = Prevent deletion of the referenced object

    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Utilma modificacion")


    class Meta:
        verbose_name = 'Inmueble'
        verbose_name_plural = 'Inmuebles'
        ordering = ["-created"]


    def __str__(self):
        return self.titulo
