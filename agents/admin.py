from django.contrib import admin
from .models import Agent

# Register your models here.
class AgentAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Agent)