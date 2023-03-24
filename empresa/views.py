from django.shortcuts import render, HttpResponse, redirect
from .models import Tecnologias, Empresa
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
def nova_empresa(request):
    if request.method == "GET":
        techs = Tecnologias.objects.all()
        return render(request, 'nova_empresa.html', {'techs': techs})
    
    elif request.method == "POST":
        nome            = request.POST.get('nome')
        email           = request.POST.get('email')
        cidade          = request.POST.get('cidade')
        endereco        = request.POST.get('endereco')
        nicho           = request.POST.get('nicho')
        tecnologias     = request.POST.getlist('tecnologias')
        caracteristicas = request.POST.get('caracteristicas')
        logo            = request.FILES.get('logo')

        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(cidade.strip()) == 0 or len(endereco.strip()) == 0 or len(tecnologias.strip()) == 0 or len(caracteristicas.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Não pode conter espaços vazios')
            return redirect('/nova_empresa')

        if logo.size > 100_000_000:
            messages.add_message(request, constants.ERROR, 'A logo da empresa deve ter menos de 10MB')
            return redirect('/nova_empresa')
        
        if nicho not in [i[0] for i in Empresa.choices_nicho_mercado]:
            messages.add_message(request, constants.ERROR, 'Nicho de mercado inválido')
            return redirect('/nova_empresa')

