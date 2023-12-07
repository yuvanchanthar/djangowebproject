from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    #template=loader_template('index.html')
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')
def html(request):
    return render(request,'html.html')
def css(request):
    return render(request,'css.html')
def java(request):
    return render(request,'js.html')



# Create your views here.
