from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario,Automovil,Marca,Estado,Categoria


# Create your views here.
def index(request):
    return render(request,'index.html')
def nosotros(request):
    return render(request,'nosotros.html')
def autos_en_alquiler(request):
    automoviles = Automovil.objects.all()
    return render(request, 'autos_en_alquiler.html', {"automoviles": automoviles})
def desarrolladoras(request):
    return render(request,'desarrolladoras.html')
def formulario(request):
    return render(request,'formulario.html')
def login(request):
    return render(request,'login.html')
def logup(request):
    if request.method == "POST":
        usuario = Usuario(request.POST['nombre'], request.POST['email'],request.POST['contacto'],request.POST['direccion'],request.POST['contraseña'] )
        usuario.save()
        return redirect('login')
   
        
   
   
