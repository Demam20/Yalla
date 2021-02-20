from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, "hello/index.html")
 

def dody(request):
  return HttpResponse('hello,ya amar!!!!!')

def retal(request):
  return HttpResponse('hello,roro!!!!!') 

def greet(request, name):
  return render(request, "hello/greet.html", {
    "name":name.capitalize()
  })     


