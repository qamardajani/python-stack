
import show_tv
from django.shortcuts import redirect, render 
from .models import *
def ind(request):
    return redirect('/shows')
def index (request):
    context={
        "all_shows": Shows.objects.all()
    }
    return render (request,'index.html',context)

def new (request) :
    context={
        "all_shows": Shows.objects.last()
    }
    return render(request,'show.html',context)

def create(request):

    Shows.objects.create(title=request.POST['title'],
    network=request.POST['network'],
    releasedate=request.POST['releasedate'],
    desc=request.POST['desc'])
    x= Shows.objects.last()  

    return redirect ("/shows/"+str(x.id))

def data (request,id):
    context={
        "all_shows":Shows.objects.get(id=id)
    }
    return render(request,"data.html",context)
def renderedit(request,id):
    context={
        "all_shows":Shows.objects.get(id=id)
    }
    return render (request,'edit.html',context)

def edit(request,id):
    new=Shows.objects.get(id=id)
    new.title=request.POST['title']
    new.network=request.POST['network']
    new.releasedate=request.POST['releasedate']
    new.desc=request.POST['desc']
    new.save()
    return redirect(f"/shows/{new.id}")
def delete(id):
    this_show = Shows.objects.get(id=id)
    this_show.delete()
    return redirect("/shows")
