from django.shortcuts import render
import random
rand=random.randint(1,100)
def index(request):
    return render (request, "index.html")
def guess(request):
    number=int(request.POST['box'])
    if number>rand :
        return render (request ,"high.html")
    if number<rand:
        return render (request ,"low.html")
    if number == rand:
        return render (request ,"equal.html")
    return render (request ,"index.html")   