from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
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

        if (len(nome.strip()) == 0) or (len(email.strip()) == 0) or (len(cidade.strip()) == 0) or (len(endereco.strip()) == 0) or (len(caracteristicas.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Não pode conter espaços vazios')
            return redirect('/nova_empresa')

        if logo.size > 100_000_000:
            messages.add_message(request, constants.ERROR, 'A logo da empresa deve ter menos de 10MB')
            return redirect('/nova_empresa')
        
        if nicho not in [i[0] for i in Empresa.choices_nicho_mercado]:
            messages.add_message(request, constants.ERROR, 'Nicho de mercado inválido')
            return redirect('/nova_empresa')

        empresa = Empresa(logo=logo,
                          nome=nome,
                          email=email,
                          cidade=cidade,
                          endereco=endereco,
                          nicho_mercado=nicho,
                          caracteristica_empresa=caracteristicas
                          )
        empresa.save()
        empresa.tecnologias.add(*tecnologias)
        empresa.save()
        messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')
        return redirect('/nova_empresa')
    

def empresas(request):
    tecnologias_filtrar = request.GET.get('tecnologias')
    nome_filtar = request.GET.get('nome')
    empresas = Empresa.objects.all()

    if tecnologias_filtrar:
        empresas = empresas.filter(tecnologias=tecnologias_filtrar)

    if nome_filtar:
        empresas = empresas.filter(nome__icontains=nome_filtar)


    
    tecnologias = Tecnologias.objects.all()

    context = {
        "empresas": empresas,
        "tecnologias": tecnologias
    }

    return render(request, 'empresas.html', context)

'''def empresas(request):
    empresas = Empresa.objects.all()

    return render(request, 'empresas.html', {'empresas': empresas})'''

def excluir_empresa(request, id):
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    messages.add_message(request, constants.SUCCESS, 'Empresa exluida com sucesso.')
    return redirect('/empresas')

def empresa(request, id):
    empresa_unica = get_object_or_404(Empresa, id=id)
    empresas = Empresa.objects.all()
    tecnologias = Tecnologias.objects.all()
    return render(request, 'empresa_unica.html', {'empresa': empresa_unica, 'tecnologias': tecnologias, 'empresas': empresas})
