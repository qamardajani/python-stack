from django.shortcuts import redirect, render, HttpResponse
def index(request):
    if 'counter' in request.session:
        request.session['counter']+=1
    else:
        request.session['counter']=0
    return render (request,"index.html")
def destroy(request):
    request.session.clear()
    return redirect ('/')
