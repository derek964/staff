from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
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
    username = request.user
    userinfo = student.objects.filter(username=username)
    selcourse = student.objects.filter(username=username).values('score__cno', 'score__cno__cname', 'score__cno__ccredit',
                                                                 'score__cno__ctime', 'score__cno__cplace', 'score__cno__tno_id__tname')
    return render(request, 'stuinfo.html', context=locals())

@login_required
@permission_required('stumgr.change_student')
def selcourse(request):
    if request.method == 'POST' and request.POST:
        cno = request.POST['cno']
        username = request.user
        user = student.objects.get(username=username)
        sno = user.sno
        #判断当前课程是否已经选修
        selected = score.objects.filter(cno_id=cno, sno_id=sno)
        #记录已选择课程数量，counted.count()直接统计数字
        counted = score.objects.filter(sno_id=sno)
        if selected:
            result = '课程已选修，请勿重复选择！'
            return JsonResponse({'result':result})
        elif counted.count() > 2:
            result = '已达到最大选修课程数量!'
            return JsonResponse({'result': result})
        else:
            #选课成功，写入数据库
            score.objects.create(cno_id=cno, sno_id=sno)
            result = 'True'
            return JsonResponse({'result': result})
    courseinfo = course.objects.all()
    return render(request, 'selcourse.html', context=locals())

@login_required
@permission_required('stumgr.change_student')
def delcourse(request):
    if request.method == 'POST' and request.POST:
        cno = request.POST['cno']
        username = request.user
        user = student.objects.get(username=username)
        sno = user.sno
        #判断当前要删除的课程是否已经选择
        selected = score.objects.filter(cno_id=cno, sno_id=sno)
        if selected:
            score.objects.filter(cno_id=cno, sno_id=sno).delete()
            result = 'True'
            return JsonResponse({'result':result})
        else:
            #课程未选择，返回错误
            result = '课程未选修，无法删除!'
            return JsonResponse({'result': result})
    # courseinfo = course.objects.all()
    # return render(request, 'selcourse.html', context=locals())

@login_required
@permission_required('stumgr.change_student')
def queryscore(request):
    username = request.user
    score = student.objects.filter(username=username).values('score__cno', 'score__cno__cname', 'score__cscore')
    return render(request, 'queryscore.html', context=locals())

@login_required
@permission_required('stumgr.change_student')
def changepassword(request):
    if request.method == 'POST' and request.POST:
        oldpassword = request.POST['oldpassword']
        newpassword2 = request.POST['newpassword2']
        username = request.session['username']
        userinfo = auth.authenticate(username=username, password=oldpassword)
        if userinfo:
            user = User.objects.get(username=username)
            user.set_password(newpassword2)
            user.save()
            result = True
            userinfo = auth.authenticate(username=username, password=newpassword2)
            auth.login(request, userinfo)
            return JsonResponse({'result': result})
        else:
            result = False
            return JsonResponse({'result': result})
#
# def mopasswd(request):
#     if request.method == 'POST' and request.POST:
#         oldpassword = request.POST['oldpassword']
#         newpassword1 = request.POST['newpassword1']
#         newpassword2 = request.POST['newpassword2']
#         username = request.user
#         userinfo = auth.authenticate(username=username, password=oldpassword)
#         if userinfo and newpassword1 == newpassword2:
#             user = User.objects.get(username=username)
#             user.set_password(newpassword2)
#             user.save()
#             return render(request, 'mopasswd.html')
#     return render(request, 'mopasswd.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@login_required
@permission_required('stumgr.change_teacher')
def tchinfo(request):
    username = request.user
    userinfo = teacher.objects.filter(username=username)
    return render(request, 'tchinfo.html', context=locals())

@login_required
@permission_required('stumgr.change_teacher')
def editscore(request):
    if request.method=='POST' and request.POST:
        cno = request.POST['cno']
        sno = request.POST['sno']
        cscore = request.POST['cscore']
        print(cscore)
        score.objects.filter(cno_id=cno, sno_id=sno).update(cscore=cscore)
        result = 'True'
        return JsonResponse({'result': result})
    username = request.user
    scored = teacher.objects.filter(username=username).values('course__cno', 'course__cname', 'course__score__sno',
                                                            'course__score__sno', 'course__score__sno_id__username',
                                                            'course__score__sno_id__sdept', 'course__score__cscore')
    return render(request, 'editscore.html', context=locals())

# @login_required
# @permission_required('stumgr.change_teacher')
# def motchpasswd(request):
#     if request.method == "POST" and request.POST:
#         oldpassword = request.POST['oldpassword']
#         newpassword1 = request.POST['newpassword1']
#         newpassword2 = request.POST['newpassword2']
#         username = request.user
#         userinfo = auth.authenticate(username=username, password=oldpassword)
#         if userinfo and newpassword1 == newpassword2:
#             user = User.objects.get(username=username)
#             user.set_password(newpassword2)
#             user.save()
#             return render(request, 'motchpasswd.html')
#     return render(request, 'motchpasswd.html')
