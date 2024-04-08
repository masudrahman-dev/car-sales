from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

from django.http import HttpResponse
from django.template import loader

from .models import Question


def detail(request, question_id):
    latest_question_list = Question.objects.all()
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }

    return HttpResponse(template.render(context, request))

def results(request, question_id):
    response = "You are looking at the results view  %s"
    # return HttpResponse(response % question_id)
    return render(request, 'polls/index.html', {"obj": "data"})


def vote(request, question_id):
    return HttpResponse("You are looking at the votes view  %s")


def index(request):
    return HttpResponse("Hello, Server is Running")
