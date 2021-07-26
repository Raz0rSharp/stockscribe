from django.shortcuts import render
from .models import Subscription
from django.http import HttpResponseRedirect
from yahoo_fin import stock_info as si
import re
#import schedule, time
from django.core.mail import send_mail

# Create your views here.
def subscribeView(request):
    subscriptions = Subscription.objects.all()
    prices = []
    for sub in subscriptions:
        prices.append({'id':sub.id, 'price': "{:,}".format(round(si.get_live_price(sub.ticker), 2))})
    return render(request, 'subscribe.html',
    {'subscriptions': subscriptions, 'prices': prices})

def addSubscriptionView(request):
    x = request.POST['ticker'].lower()
    y = request.POST['email']
    valid_ticker = checkTickerValidity(x)
    valid_email = checkEmailValidity(y)
    if (valid_email and valid_ticker):
    #yahoo finance API
        new_item = Subscription(ticker = x, email = y)
        new_item.save()
    return HttpResponseRedirect('/')

def deleteSubscriptionView(request, s):
    y = Subscription.objects.get(id= s)
    y.delete()
    return HttpResponseRedirect('/')

def sendNowView(request, s):
    y = Subscription.objects.get(id=s)
    send_mail(
    'Your Stock Subscription',
    y.ticker +': $' + "{:,}".format(round(si.get_live_price(y.ticker), 2)),
    'nick.lesho@gmail.com',
    [y.email],
    fail_silently=False,
    )
    return HttpResponseRedirect('/')

def checkEmailValidity(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.match(regex, email)):
        return True
    else:
        return False

def checkTickerValidity(ticker):
    try:
        si.get_live_price(ticker)
    except AssertionError:
        return False
    return True
