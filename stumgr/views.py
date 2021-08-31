from django.shortcuts import render
from django.http import HttpResponseRedirect
from stumgr.models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index(request):
    if request.method == 'POST' and request.POST:
        username = request.POST['username']
        password = request.POST['password']
        userinfo = auth.authenticate(username=username, password=password)
        if userinfo:
            auth.login(request, userinfo)
            stuinfo = student.objects.filter(username=username)
            if stuinfo:
                return HttpResponseRedirect('/stuinfo/')
            else:
                return HttpResponseRedirect('/tchinfo/')
    return render(request, 'index.html')

@login_required
@permission_required('stumgr.change_student')
def stuinfo(request):
    return render(request, 'stuinfo.html')

@login_required
@permission_required('stumgr.change_student')
def selcourse(request):
    return render(request, 'selcourse.html')

@login_required
@permission_required('stumgr.change_student')
def queryscore(request):
    return render(request, 'queryscore.html')

@login_required
@permission_required('stumgr.change_student')
def mopasswd(request):
    if request.method == 'POST' and request.POST:
        oldpassword = request.POST['oldpassword']
        newpassword1 = request.POST['newpassword1']
        newpassword2 = request.POST['newpassword2']
        username = request.user
        userinfo = auth.authenticate(username=username, password=oldpassword)
        if userinfo and newpassword1 == newpassword2:
            user = User.objects.get(username=username)
            user.set_password(newpassword2)
            user.save()
            return render(request, 'mopasswd.html')
    return render(request, 'mopasswd.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@login_required
@permission_required('stumgr.change_teacher')
def tchinfo(request):
    return render(request, 'tchinfo.html')

@login_required
@permission_required('stumgr.change_teacher')
def editscore(request):
    return render(request, 'editscore.html')

@login_required
@permission_required('stumgr.change_teacher')
def motchpasswd(request):
    if request.method == "post" and request.POST:
        oldpassword = request.POST['oldpassword']
        newpassword1 = request.POST['newpassword1']
        newpassword2 = request.POST['newpassword2']
        username = request.user
        userinfo = auth.authenticate(username=username, password=oldpassword)
        if userinfo and newpassword1 == newpassword2:
            user = User.objects.get(username=username)
            user.set_password(newpassword2)
            user.save()
            return render(request, 'motchpasswd.html')
    return render(request, 'motchpasswd.html')
