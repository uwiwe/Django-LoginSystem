from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, checkpassword
from .forms import UsuarioForm
import logging

logger = logging.getLogger(__name__)

def main(request):
  mydata = Usuario.objects.all()
  return render(request, 'main.html', {'mydata': mydata})

def register(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado con éxito.')
            return redirect('main')
        else:
            messages.error(request, 'Error en el registro. Verifica los campos.')
    else:
        form = UsuarioForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión correctamente.')
            return HttpResponseRedirect('/profile/')
        else:
            messages.error(request, 'Error: nombre de usuario o contraseña no válida.')
            return HttpResponseRedirect('/login/')

    return render(request, 'login.html')

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})