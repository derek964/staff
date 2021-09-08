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
