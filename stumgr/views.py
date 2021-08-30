from django.shortcuts import render
from django.http import HttpResponseRedirect
from stumgr.models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.method == 'POST' and request.POST:
        username = request.POST['username']
        password = request.POST['password']
        userinfo = auth.authenticate(username=username, password=password)
        if userinfo:
            auth.login(request, userinfo)
            request.session['username'] = username
            return HttpResponseRedirect('/stuinfo/')
        else:
            return HttpResponseRedirect('/tchinfo/')
    return render(request, 'index.html')

@login_required
def stuinfo(request):
    return render(request, 'stuinfo.html')

@login_required
def selcourse(request):
    return render(request, 'selcourse.html')

@login_required
def queryscore(request):
    return render(request, 'queryscore.html')

@login_required
def mopasswd(request):
    return render(request, 'mopasswd.html')

def logout(request):
    auth.logout()
    return HttpResponseRedirect('/')