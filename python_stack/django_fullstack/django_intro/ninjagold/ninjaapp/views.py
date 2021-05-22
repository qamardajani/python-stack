from django.shortcuts import redirect, render
from time import  localtime, strftime
import random
def index(request):
    if 'ninja' not in request.session:
        request.session['ninja'] = 0
    if 'activities' not in request.session:
        request.session['activities']=[]

    context = {
        "activities":request.session['activities']
    }    
    return render(request,"index.html",context)

def act(request):
    activities = request.session['activities']
    date_time = strftime("%B %d, %Y %H:%M %p",localtime())
    ninja_gold = request.session['ninja']
    place = request.POST['process']

    if "ninja" in request.session:
        if request.POST['process'] == 'farm':
            ninja_gold = random.randint(10, 20)
            request.session['ninja'] = request.session['ninja'] + ninja_gold
            print(ninja_gold)
        elif request.POST['process'] == 'cave':
            ninja_gold = random.randint(5, 10)
            request.session['ninja'] = request.session['ninja'] + ninja_gold
            print(ninja_gold)
        elif request.POST['process'] == 'house':
            ninja_gold = random.randint(2, 5)
            request.session['ninja'] = request.session['ninja'] + ninja_gold
            print(ninja_gold)
        elif request.POST['process'] == 'casino':
            ninja_gold = random.randint(-50, 50)
            request.session['ninja'] = request.session['ninja'] + ninja_gold
            print(ninja_gold)

    if ninja_gold >= 0:
        text = f"Earned {ninja_gold} golds from the {place}! ({date_time})"
            
    else:
        text = f"Entered a casino and lost {ninja_gold}...Ouch.. ({date_time})"
            
    activities.append(text)
    request.session['activities'] = activities         
    return redirect("/")

    

    