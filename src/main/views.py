from django.shortcuts import render, HttpResponse, redirect
from main.models import Repuesto
from django.db.models import Q
from main.forms import FormRepuesto

layout = """"
    <h1> Web DJango</h1>
    <hr/>
    <ul>
        <li>
            <a href = "/inicio">Inicio</a>
        </li>
        <li>
            <a href = "/metodo-1">metodows</a>
        </li>
        <li>
            <a href = "/contacto">contacto</a>
        </li>
    </ul>
    <hr/>
"""

nombre = "Reynaldo"
languages = ['Java','c++','python']
years = 2020
until = range(years,2051)

def index(request):
    
    return render(request, 'index.html', {
        't':'Inicio',
        'nombre':nombre,
        'languages':languages,
        'years':until
    })

def met1(request,redirigir=0):
    return render(request,'metodo-1.html',{
        't':'Metodo1',
        'msg':'Habla causa'
    })

def contacto(request,nombre="Reynaldo"):
    return HttpResponse(layout+f"<h2>Contacto {nombre} </h2>")

def saveRepuesto(request):
    if request.method == 'POST':
        nombre=request.POST['repuesto']
        stock=request.POST['stock']
        rep = Repuesto(
            nombre = nombre,
            stock = stock,
        )
        rep.save()
        return HttpResponse(f"Repuesto creado: {rep.nombre} - {rep.stock}")
    else:
        return HttpResponse("<h2>FUCK U BRO<h/2>")

def createRepuesto(request):
    return render(request,'createRepuesto.html')

def repuesto(request):
    try:
        repu = Repuesto.objects.get(stock=15)
        response = f"Repuesto: <br/> {repu.nombre} - {repu.stock}"
    except:
        response = "Respuesto no encontrado"
    return HttpResponse(response)

def updateRepuesto(request,id):
    rep = Repuesto.objects.get(pk=id)
    rep.nombre = "Perno3"
    rep.stock = 15
    rep.save() 
    return HttpResponse("Cambio realizado")

def listarRepuesto(request):
    rep = Repuesto.objects.all()
    '''rep = Repuesto.objects.filter(
        id__lte=5
    )
    rep = Repuesto.objects.filter(
        Q(stock__contains=1) | Q(nombre__contains="Perno")
    )'''
    #rep = Repuesto.objects.all()           orden:id asc
    #rep = Repuesto.objects.order_by('-id') orden:id des
    #rep = Repuesto.objects.order_by('-id')[:3] #solo 3 elementos [1:4]
    return render(request,'repuestos.html',{
        'rep' : rep,
        't' : 'ListaRepuestos',
        'msg' : 'Lista Repuestos',
    })

def borrarRepuesto(request,id):
    repuesto = Repuesto.objects.get(pk=id)
    repuesto.delete()

    return redirect('Lrepuesto')

def createFormRepuesto(request):
    if request.method=='POST':
        formulario=FormRepuesto(request.POST)
        if formulario.is_valid():
            data_form=formulario.cleaned_data
            nombre=data_form['nombre']
            stock=data_form['stock']
            rep = Repuesto(
                nombre = nombre,
                stock = stock,
            )
            rep.save()
            return redirect('Lrepuesto')
    else:
        formulario=FormRepuesto()

    return render(request,'createFormRepuesto.html',{
        'form':formulario
    })

#MVC modelo vista controlador
##Equivalentes
#MVT modelo template vista

# Create your views here.
