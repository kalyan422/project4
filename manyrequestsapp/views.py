from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return render(request,'home.html')
def GetInput(request):
    return render(request,'getinput.html')
def PostInput(request):
    return render(request,'postinput.html')
def Add(request):
    if request.method=="GET":
        p=int(request.GET["t1"])
        q=int(request.GET["t2"])
        r=p+q
        return HttpResponse("The sum is: "+str(r))
    else:
        X=int(request.POST["t1"])
        Y=int(request.POST["t2"])
        Z=X+Y
        return HttpResponse("The sum is :"+str(Z))