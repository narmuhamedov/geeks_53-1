from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
  if request.method == 'GET':
    return HttpResponse('Привет это мой первый проект на Django!')