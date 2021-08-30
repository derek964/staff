from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def stuinfo(request):
    return render(request,'stuinfo.html')

def selcourse(request):
    return render(request,'selcourse.html')

def queryscore(request):
    return render(request,'queryscore.html')

def mopasswd(request):
    return render(request,'mopasswd.html')