from django.db import models
from django.contrib.auth.models import User


class student(models.Model):
    sno = models.CharField(max_length=10, unique=True, primary_key=True)
    sname = models.CharField(max_length=10, null=True)
    username = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    ssex = models.CharField(max_length=10, null=True)
    sage = models.CharField(max_length=10, null=True)
    sdept = models.CharField(max_length=10, null=True)

class teacher(models.Model):
    tno = models.CharField(max_length=10, unique=True, primary_key=True)
    tname = models.CharField(max_length=10, null=True)
    username = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    ttitle = models.CharField(max_length=10, null=True)

class course(models.Model):
    cno = models.CharField(max_length=10, unique=True, primary_key=True)
    cname = models.CharField(max_length=10, null=True)
    ccredit = models.CharField(max_length=10, null=True)
    ctime = models.CharField(max_length=10, null=True)
    cplace = models.CharField(max_length=10, null=True)
    tno_id = models.ForeignKey(teacher, to_field='tno', on_delete=models.CASCADE)

class score(models.Model):
    cno = models.ForeignKey(course, to_field='cno', on_delete=models.CASCADE)
    sno = models.ForeignKey(student, to_field='sno', on_delete=models.CASCADE)
    cscore = models.IntegerField(null=True)