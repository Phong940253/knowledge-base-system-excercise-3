from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


def index(request):
    template = loader.get_template('html/Final_project.html')
    # template = loader.get_template('html/staticfile.html')
    context = {
        'latest_question_list': '',
    }
    return HttpResponse(template.render(context, request))


@api_view(['POST'])
def getMathProblem(request):
    data = JSONParser().parse(request)
    # GET all published tutorials