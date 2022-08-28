from django.shortcuts import render
import requests  
from .models import Question
from django.http import HttpResponse
# Create your views here.


def index(request):
    response = requests.get('https://www.alphavantage.co/query?function=NEWS_SENTIMENT&topics=technology&apikey=RIDUWMSKIS4518PV').json()
    composites = requests.get('https://api.twelvedata.com/price?symbol=AAPL,MSFT,CRWD,GOOG,PLTR&apikey=c486aa4073cd405daae26abe7f2aef04').json()
    # high_volume = requests.get('https://financialmodelingprep.com/api/v3/stock_market/actives?apikey=a47ede9cfb01fb619982832def1ce5cc').json()

    images = response['feed'][0]['banner_image']
    # news_image = requests.get(images)    
    context = {
        'news': response,
        # 'image': news_image,
        'composites': composites,
    }
    return render(request, 'polls/content.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)