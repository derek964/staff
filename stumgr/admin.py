from django.contrib import admin
from stumgr.models import *

# Register your models here.
class Newstudent(admin.ModelAdmin):
    list_display = ['sno', 'sname', 'username']

class Newteacher(admin.ModelAdmin):
    list_display = ['tno', 'tname', 'username']

class Newcourse(admin.ModelAdmin):
    list_display = ['cno', 'cname', 'ccredit', 'ctime', 'cplace']


admin.site.register(student)
admin.site.register(teacher)
admin.site.register(course)