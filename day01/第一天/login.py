#!/usr/bin/python
# -*- coding:utf-8 -*-

#读取文件
f1 = open('db','r')
data = f1.read()
f1.close()

#print(data)
#初始化变量
user_info_list = []
user_str_list = data.split('\n')
#print(user_info_list)


#格式化 数据
for i in user_str_list:
 #   print(i)
    temp = i.split('|')
#    print(temp)
    v = {
        'name': temp[0],
         'pwd':temp[1],
        'time':temp[2]
    }
    user_info_list.append(v)
#print(user_info_list)

fist_time =1


while True:
    ##输入用户名密码
    user_name = input('请输入用户名:')
    password = input('请输入密码:')
    print(user_name,password)
    ##判断是否为空
    if user_name == '' or password == '':
        print('用户名或密码不能为空')
        continue
    #获取用户名密码
    for user_dic in user_info_list:
        name = user_dic['name']
        pwd = user_dic['pwd']
       # print(user_dic['time'])
        # if fist_time == 1 :
        #     time = user_dic['time']
        #fist_time = fist_time + 1
        #判断登录规则
        if user_name == name:
            ##判断 输入错误的次数
            if fist_time == 1:
                time = user_dic['time']
                fist_time = fist_time + 1
            if int(time) >= 3:
                print('该账户重新输入密码超过三次已经被锁定，请联系管理员')
                #更新文件
                print(user_info_list)
                exit()
            if password == pwd:
                print("登录成功")
                time = 0
                #更新文件
                exit()
            else:
                #数据错误密码  更新time
                time = int(time) +1
                print(time)
                break
    print('用户名或密码错误,请重新输入')





