from time import time
from django.shortcuts import render
import requests  
from .models import Question
import pandas
from django.http import HttpResponse
import plotly.graph_objects as go
import plotly.offline as py
from plotly.offline import plot
import plotly.graph_objs as go

# Create your views here.


def index(request):
    response = requests.get('https://www.alphavantage.co/query?function=NEWS_SENTIMENT&topics=technology&apikey=RIDUWMSKIS4518PV').json()
    composites = requests.get('https://api.twelvedata.com/price?symbol=NVDA,TSLA,AAPL,MSFT,CRWD,GOOG,PLTR&apikey=c486aa4073cd405daae26abe7f2aef04').json()
    high_volume = requests.get('https://financialmodelingprep.com/api/v3/stock_market/actives?apikey=a47ede9cfb01fb619982832def1ce5cc').json()
    

    context = {
        'news': response,
        'composites': composites,
        "hi_volume": high_volume,
        "graphs": graphs()
    }
    return render(request, 'polls/content.html', context)

def graphs(): 
    response = requests.get('https://financialmodelingprep.com/api/v3/historical-chart/30min/AAPL?apikey=a47ede9cfb01fb619982832def1ce5cc').json()
    price_list = []
    for value in response: 
        price_list.append(value["open"])
    return price_list

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)