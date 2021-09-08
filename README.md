# staff

简单的学生选课管理系统

1、用户包括学生、老师、管理员。

2、管理员有单独的登录门户，登录后可以创建学生、老师、课程，并且指定课程的授课老师。

3、学生与老师统一登录门户，但是不同的身份登录后，会跳转到不同的页面。

4、学生登录后页面包括如下功能：

1）个人信息：登录后显示学生个人信息

2）学生选课：学生可以看到课程名、授课老师、上课时间，点击选课，可以选取课程，最多两门（超过不能继续选课），同一门课程不能重复选。

3）成绩查询：查询已选课程的成绩

4）修改密码：修改用户密码

5）注销：注销后自动返回登录页面

5、老师登录后页面包括如下功能：

1）个人信息：登录后显示老师个人信息，以及自己需要授课的课程名、上课时间、上课地点。

2）成绩录入：可以查看自己授课的课程下面的学生，并且可以录入成绩，成绩仅能为0~100分，超出范围会提示无效，可以多次修改成绩。

3）修改密码：修改用户密码

4）注销：注销后自动返回登录页面

6、管理员登录后，页面包括如下功能：

1）创建用户

2）创建用户组

3）创建课程与授课老师

增加用户：testuser，密码：derek@123

注意:
1、html中form里的表格名称不要用id，用name（修改密码的页面时时需要修改代码）
2、在获取用户用户名的时候，不用username = request.session['username']，而是用了username = request.user