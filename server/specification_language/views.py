from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .transform import Transform
from django.http import JsonResponse


def index(request):
    template = loader.get_template('html/Final_project.html')
    # template = loader.get_template('html/staticfile.html')
    context = {
        'latest_question_list': '',
    }
    return HttpResponse(template.render(context, request))


@api_view(['POST'])
def pushMathProblem(request):
    problem = request.POST.get("problem", "")
    problem = problem.replace("\r\n", "")
    transform = Transform()
    result = transform.transformAll(problem)

    template = loader.get_template('html/Final_project.html')
    # template = loader.get_template('html/staticfile.html')

    response_data = {}
    response_data['result'] = result
    response_data['message'] = 'Some error message'
    response_data['success'] = True

    return JsonResponse(response_data)
    # GET all published tutorials