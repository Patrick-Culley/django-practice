import requests  
from .forms import searchForm
from time import time
from django.shortcuts import render
from .models import Question
from django.http import HttpResponse
import math 
 
# Create your views here.

def index(request):
    response = requests.get('https://www.alphavantage.co/query?function=NEWS_SENTIMENT&topics=technology&apikey=RIDUWMSKIS4518PV').json()
    composites = requests.get('https://api.twelvedata.com/price?symbol=NVDA,TSLA,AAPL,MSFT,CRWD,GOOG,PLTR&apikey=c486aa4073cd405daae26abe7f2aef04').json()
    high_volume = requests.get('https://financialmodelingprep.com/api/v3/stock_market/actives?apikey=a47ede9cfb01fb619982832def1ce5cc').json()
    key_stats = requests.get('https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=a47ede9cfb01fb619982832def1ce5cc').json()

    context = {
        'news': response,
        'composites': composites,
        "hi_volume": high_volume,
        "graphs": graphs()[0],
        "interval": graphs()[1],
        "key_stats": key_stats
    }
    return render(request, 'polls/content.html', context)

def graphs(): 
    response = requests.get('https://financialmodelingprep.com/api/v3/historical-chart/30min/AAPL?apikey=a47ede9cfb01fb619982832def1ce5cc').json()
    price_list = []
    date_list = []
    for value in response: 
        price_list.append(value["open"])
        date_list.append(value["date"])
    return [price_list, date_list]

def search(request):
    ticker = request.GET.get("search")
    response = requests.get('https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker.upper() + '&apikey=RIDUWMSKIS4518PV').json()
    news = requests.get('https://www.alphavantage.co/query?function=NEWS_SENTIMENT&topics=technology&apikey=RIDUWMSKIS4518PV').json()

    metrics = {
        "news": news["feed"],
        "symbol": ticker.upper(),
        "summary": response["Description"],
        "m_cap": conversions(response["MarketCapitalization"]), 
        "peRatio": response["PERatio"],
        "eps": response["EPS"],
        "52weekhigh": response["52WeekHigh"],
        "52weeklow": response["52WeekLow"],
        "targetprice": response["AnalystTargetPrice"],
        "margin": response["ProfitMargin"],
        "beta": response["Beta"], 
        "div_yield": response["DividendYield"],
        "DivDate": response["ExDividendDate"]

    }

    return render(request, 'polls/search.html', {'form': metrics})

def conversions(value): 
    first = list(value)
    if len(value) >= 13: 
        first.insert(1, ".")
        return (''.join(first))[:4] + " trillion"
    elif len(value) < 13 and len(value) > 6: 
        if len(value) == 12:
            first.insert(3, ".")
            return (''.join(first))[:6] + " billion"
        elif len(value) == 11:
            first.insert(2, ".")
            return (''.join(first))[:5] + " billion"
        else: 
            first.insert(1,".")
            return (''.join(first))[:4] + " billion"
    else: 
        if len(value) == 9:
            first.insert(3, ".")
            return (''.join(first))[:6] + " million"
        elif len(value) == 8:
            first.insert(2, ".")
            return (''.join(first))[:5] + " million"
        else: 
            first.insert(1,".")
            return (''.join(first))[:4] + " million"


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)