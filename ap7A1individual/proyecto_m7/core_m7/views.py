from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from core_m7.forms.formulario import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


# Create your views here.
def index_welcome(request):
    return render(request, 'welcome.html')


class BienvenidaView(TemplateView):
    template_name = "bienvenida_login.html"
    
class TareasView(TemplateView):
    template_name = "tareas.html"
    
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("Formulario Valido")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    print("Usuario activo")
                    login(request, user)
                    return redirect('http://127.0.0.1:8000/')

                else:
                    print("Usuario inactivo")
                    return HttpResponse('Cuenta deshabilitada')
            else:
                print("Usuario o contraseña incorrectos")
                return HttpResponse('Login no Valido')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



    
