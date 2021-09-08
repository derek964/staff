//修改密码的函数
function changepassword() {
    if ($('#oldpassword').val() == '' || $('#newpassword1').val() == '' || $('#newpassword2').val() == '') {
        $("#newpasswordinfo").text("密码不能为空！");
    } else if ($('#newpassword1').val() != $('#newpassword2').val()) {
        $("#newpasswordinfo").text("两次输入的新密码不一致！");
    } else {
        $.post('/changepassword/', {
            'oldpassword': $('#oldpassword').val(),
            'newpassword1': $('#newpassword1').val(),
            'newpassword2': $('#newpassword2').val(),
        }, function (res) {
            if(res.result){
                alert("修改成功！");
                window.location.reload();
            }else{
                alert("旧密码不正确，请重新输入！");
                window.location.reload();
            }
        }, 'json')
    }
};

//删除课程函数
function delcourse(cno) {
        $.post('/delcourse/', {
            'cno':cno,
        }, function (res) {
            if(res.result=='True'){
                alert("删除成功！");
                window.location.reload();
            }else{
                alert(res.result);
                window.location.reload();
            }
        }, 'json')
}

//增加课程函数
function addcourse(cno) {
        $.post('/selcourse/', {
            'cno':cno,
        }, function (res) {
            if(res.result=='True'){
                alert("选课成功！");
                window.location.reload();
            }else{
                alert(res.result);
                window.location.reload();
            }
        }, 'json')
}


//editscore的函数
function editscore(cno,sno,cscore){
    var d = dialog({
            width: 360,
            title: '成绩录入',
            quickClose: true,
            content: '<label class="col-sm-3 control-label bk-lh30 pt0">成绩：</label>' +
                '<div class="col-sm-9">' +
                '<input type="text" class="form-control bk-valign-top" id="scored" placeholder=""> ' +
                '</div>',
            ok: function() {
                    $.post('/editscore/', {
                    'cno': cno,
                    'sno': sno,
                    'cscore': $('#scored').val(),
                }, function (res) {
                    if (res.result == 'True') {
                        alert("修改成功");
                        window.location.reload();
                    } else {
                        alert("修改失败");
                        window.location.reload();
                    }
                }, 'json')
            },
            cancelValue: '取消',
            cancel: function() {
                console.log(this)
                // do something
            },
            onshow: function() {
                $('#scored').val(cscore);
                // do something
            }
        });
        d.show();
    }