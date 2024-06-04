from django.shortcuts import render
from django.http import HttpResponse
import datetime
def time(request):
    now = datetime.datetime.now()
    return HttpResponse('<H2>Time Now : </H2>'+str(now))