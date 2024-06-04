from django.shortcuts import render
from django.http import HttpResponse

def wish(request):
    message='<h1>Hi buddy </h1>'
    return HttpResponse(message)
