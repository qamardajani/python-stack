from django.http.response import HttpResponse
from django.shortcuts import render , HttpResponse

def index(request):
    return render(request, "index.html")
    
def result(request):
    
   
        user_name = request.POST['name']
        user_location = request.POST['locate']
        user_lang = request.POST['language']
        user_mess = request.POST['message']
        context = {
        "user_name_temp": user_name, 
        "user_location_temp": user_location,
         "user_lang_temp": user_lang,
          "user_mess_temp": user_mess
    
        }
        return render(request,"show.html",context)

