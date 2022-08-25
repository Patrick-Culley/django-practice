from django.shortcuts import render
import requests  
from .models import Question
from django.http import HttpResponse
# Create your views here.


def index(request):
    response = requests.get('https://www.alphavantage.co/query?function=NEWS_SENTIMENT&topics=technology&apikey=RIDUWMSKIS4518PV').json()
    return render(request, 'polls/index.html', {'response':response})

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)