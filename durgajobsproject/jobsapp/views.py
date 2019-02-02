from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobsinfo(request):
     s='<h1>this gives information about hyderabad jobs</h1>'
     return HttpResponse(s)
def bngjobsinfo(request):
     s='<h1>this gives information about bangalore jobs</h1>'
     return HttpResponse(s)
def punejobsinfo(request):
     s='<h1>this gives information about pune jobs</h1>'
     return HttpResponse(s)
