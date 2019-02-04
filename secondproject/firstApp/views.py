from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def tim(request):
    date=datetime.datetime.now()
    s='<h1>welcome to you !!!!</h1><hr>'
    s=s+'<h1>now the time is:'+str(date)+'</h1>'
    return HttpResponse(s)
