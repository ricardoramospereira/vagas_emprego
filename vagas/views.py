from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, Http404
from django.contrib import messages
from django.contrib.messages import constants
from empresa.models import Vagas
from vagas.models import Tarefa


# Create your views here.
def nova_vaga(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        email = request.POST.get('email')
        tecnologias_domina = request.POST.getlist('tecnologias_domina')
        tecnologias_nao_domina = request.POST.getlist('tecnologias_nao_domina')
        experiencia = request.POST.get('experiencia')
        data_final = request.POST.get('data_final')
        empresa = request.POST.get('empresa')
        status = request.POST.get('status')

        vaga = Vagas(
            titulo = titulo,
            email = email,
            nivel_experiencia = experiencia,
            data_final = data_final,
            empresa_id = empresa,
            status = status,
        )

        vaga.save()

        vaga.tecnologias_estudar.add(*tecnologias_nao_domina)
        vaga.tecnologias_dominadas.add(*tecnologias_domina)

        vaga.save()

        messages.add_message(request, constants.SUCCESS, 'Vaga cadastrada com sucesso')
        return redirect(f'/empresa/{empresa}')
      
    # validações
    
    #######################

    elif request.method == "GET":
        raise Http404


def vaga(request, id):
    vaga = get_object_or_404(Vagas, id=id)
    tarefas = Tarefa.objects.filter(vaga=vaga).filter(realizada=False)
    return render(request, 'vaga.html', {'vaga': vaga, 'tarefas': tarefas,})

def nova_tarefa(request, id_vaga):
    titulo = request.POST.get('titulo')
    prioridade = request.POST.get("prioridade")
    data = request.POST.get('data')
    
    tarefa = Tarefa(vaga_id=id_vaga,
                    titulo=titulo,
                    prioridade=prioridade,
                    data=data)
    tarefa.save()
    messages.add_message(request, constants.SUCCESS, 'Tarefa criada com sucesso')
    return redirect(f'/vagas/vaga/{id_vaga}')

def realizar_tarefa(request, id):
    tarefas_list = Tarefa.objects.filter(id=id).filter(realizada=False)

    if not tarefas_list.exists():
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema!')
        return redirect(f'/home/empresas/')

    tarefa = tarefas_list.first()
    tarefa.realizada = True
    tarefa.save()    
    messages.add_message(request, constants.SUCCESS, 'Tarefa realizada com sucesso, parabéns!')
    return redirect(f'/vagas/vaga/{tarefa.vaga.id}')