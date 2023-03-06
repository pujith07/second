from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def koti(request):
    return HttpResponse('<marquee><h1>koti is a fan of NTR</h1></marquee>')
def prakash(request):
    return HttpResponse('prakash is fan of Rajini kanth')
def pujith(request):
    return HttpResponse('pujith is a fan mb')