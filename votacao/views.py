
# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Questao
from django.template import loader
from django.http import Http404

#def index(request):
#    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
#    template = loader.get_template('votacao/index.html')
#    context = { 'latest_question_list': latest_question_list, }
#    return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'votacao/index.html', context)

#def detalhe(request, questao_id):
#    return HttpResponse("Esta e a questao %s." % questao_id)

#def detalhe(request, questao_id):
#    try:
#        questao = Questao.objects.get(pk=questao_id)
#    except Questao.DoesNotExist:
#        raise Http404("A questao nao existe")
#    return render(request, 'votacao/detalhe.html', {'questao': questao})


def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/detalhe.html', {'questao': questao})

#<li>
#<a href = "/votacao/{{ questao.id }}" >
#{{questao.questao_texto}}
#</a>
#</li>

def resultados(request, questao_id):
    response = "Estes sao os resultados da questao %s."
    return HttpResponse(response % questao_id)
def voto(request, questao_id):
    return HttpResponse("Votacao na questao %s." % questao_id)
