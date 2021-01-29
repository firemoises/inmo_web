from django.contrib import admin
from .models import Inmueble

# Register your models here.
class InmuebleAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Inmueble)