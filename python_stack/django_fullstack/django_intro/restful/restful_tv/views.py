from django.http.response import HttpResponse
from django.shortcuts import render , HttpResponse
from .models import *

def index (request):
    context={
        "all_shows" : Shows.objects.all()
    }
    return render (request,'index.html',context)
  