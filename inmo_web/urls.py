"""inmo_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from core import views

from django.conf import settings # Para traernos las variables de settings

urlpatterns = [
    path('', views.home, name="home"),
    path('portfolio/<int:portfolio_id>/', views.portfolio, name="portfolio"),
    path('agents/<int:agents_id>/', views.agents, name="agents"),
    path('prueba/', views.prueba, name="prueba"),
    path('admin/', admin.site.urls),
]

#Para poder ver media files en entorno de desarrollo
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)