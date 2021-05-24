from dojoapp.models import Dojo, Ninja
import re
from django.http.response import HttpResponse
from django.shortcuts import render , redirect

def index(request):
    
    context = {"dojos" : Dojo.objects.all(),
            "ninjaa" : Ninja.objects.all()
    }		
    return render(request, "index.html",context)
def add(request):
    Dojo.objects.create(name=request.POST['Name'],city=request.POST['city'] , state=request.POST['state'])
    return redirect('/')
def add1(request):
    Ninja.objects.create(first_name=request.POST['First_Name'] , last_name=request.POST['last_Name'],Dojo_id=Dojo.objects.get(id =request.POST['dojo']))
    return redirect('/')
