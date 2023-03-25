from django.shortcuts import render, redirect
from django.http import HttpRequest, Http404
from django.contrib import messages
from django.contrib.messages import constants


# Create your views here.
def nova_vaga(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        email = request.POST.get('email')
        tecnologias_domina = request.POST.get('tecnologias_domina')
        tecnologias_nao_domina = request.POST.get('tecnologias_nao_domina')
        experiencia = request.POST.get('experiencia')
        data_final = request.POST.get('data_final')
        empresa = request.POST.get('empresa')
        status = request.POST.get('status')
      
    # validações
    
    #######################

    elif request.method == "GET":
        raise Http404
