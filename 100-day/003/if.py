username = str(input("请输入用户名 \n"))
password = str(input("请输入密码 \n"))

if username == 'admin' and password == '123456':
    print("登录成功！")
else:
    print("登录失败！")
