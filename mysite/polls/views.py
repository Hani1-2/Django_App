from django.http import HttpResponse
from django.shortcuts import render


def index(request):
  context = {
    'variable' : 'This is sent message'
  }
  return render(request,'index.html',context)
    #HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
def about(request):
  context = {
    'variable' : 'This is sent message'
  }
  return render(request,'about.html',context)
def contact(request):
  context = {
    'variable' : 'This is sent message'
  }
  return render(request,'contact.html',context)