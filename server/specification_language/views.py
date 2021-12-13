from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('html/Final_project.html')
    context = {
        'latest_question_list': '',
    }
    return HttpResponse(template.render(context, request))
