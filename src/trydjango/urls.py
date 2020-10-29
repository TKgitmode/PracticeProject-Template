"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#se importa los urls de la app propia
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('',views.index,name='index'),
    path('inicio/',views.index,name='inicio'),
    path('metodo-1/', views.met1 ,name="prueba1"),
    path('metodo-1/<int:redirigir>', views.met1 ,name="prueba1"),
    path('contacto/<str:nombre>',views.contacto, name="contacto"),
    path('contacto/',views.contacto, name="contacto"),
    path('repuesto/',views.repuesto, name="repuesto"),
    path('updateRepuesto/<int:id>',views.updateRepuesto, name="repuesto"),
    path('listaRepuestos/',views.listarRepuesto, name="Lrepuesto"),
    path('borrarRepuesto/<int:id>',views.borrarRepuesto, name="Brepuesto"),
    path('saveRepuesto/',views.saveRepuesto, name="Srepuesto"),
    path('createRepuesto/',views.createRepuesto, name="Crepuesto"),
    path('createFormRepuesto/',views.createFormRepuesto, name="CFrepuesto")
]
