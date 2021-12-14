from django.urls import path
from django.views.generic.base import View

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('push', views.pushMathProblem, name='push'),
]
