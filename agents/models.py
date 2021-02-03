from django.db import models

# Create your models here.
class Agent(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    correo2 = models.EmailField(max_length=100, blank=True)
    telefono = models.PositiveIntegerField()
    telefono2 = models.PositiveIntegerField(default="8099689333")
    #telefono3 = models.PositiveIntegerField(default="8099689333")
    testfield = models.PositiveIntegerField(default="8099689333")

    url_facebook = models.URLField(blank=True)
    url_twitter = models.URLField(blank=True)
    url_instagram = models.URLField(blank=True)
    url_linkedin = models.URLField(blank=True)
    url_youtube = models.URLField(blank=True)

    desc = models.TextField(verbose_name="Descripcion")

    image1 = models.ImageField(verbose_name="Imagen 1", upload_to="Agentes", blank=True)
    image2 = models.ImageField(verbose_name="Imagen 2", upload_to="Agentes", blank=True)
    image3 = models.ImageField(verbose_name="Imagen 3", upload_to="Agentes", blank=True)
    image4 = models.ImageField(verbose_name="Imagen 4", upload_to="Agentes", blank=True)
    image5 = models.ImageField(verbose_name="Imagen 5", upload_to="Agentes", blank=True)
   
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Utilma modificacion")


    class Meta:
        verbose_name = 'Agente'
        verbose_name_plural = 'Agentes'
        ordering = ["-created"]


    def __str__(self):
        return self.nombre
