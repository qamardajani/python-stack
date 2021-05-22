from django.http.response import HttpResponse
from django.shortcuts import redirect, render 
from .models import users
def index(request):
    context = {
    	"all_the_users": users.objects.all()
    }
    return render(request, "index.html", context)
def add(request):
    users.objects.create(first_name=request.POST['First Name'],last_name=request.POST['last Name'],email_address=request.POST['email'],age=request.POST['age'])
    return redirect('/')

def get(request , id):
    context = {
    "first_name" : users.objects.get(id=id)
    }
    return render (request,"show.html",context)