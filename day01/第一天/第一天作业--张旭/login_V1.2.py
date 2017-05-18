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
# print(user_str_list)
id = 0

#格式化 数据
for i in user_str_list:
    if i == '':
        break
    temp = i.split('|')
    # print(temp)
    v = {
        'id': id,
        'name': temp[0],
         'pwd':temp[1],
        'time':temp[2]

    }
    id = id + 1
    user_info_list.append(v)
#print(user_info_list)


#判断 多次重试后的次数  取消  不能判断俩个 用户重试
#fist_time =1


while True:
    ##输入用户名密码
    user_name = input('请输入用户名:')
    password = input('请输入密码:')
    #print(user_name,password)
    ##判断是否为空
    if user_name == '' or password == '':
        print('用户名或密码不能为空')
        continue
    #获取用户名密码
    #print(user_info_list)
    for user_dic in user_info_list:
        name = user_dic['name']
        pwd = user_dic['pwd']
        time = user_dic['time']
        id = user_dic['id']
        # if fist_time == 1 :
        #     time = user_dic['time']
        #fist_time = fist_time + 1
        #判断登录规则
        if user_name == name:
            ##判断 输入错误的次数
            # 判断 多次重试后的次数  取消  不能判断俩个 用户重试
            #if fist_time == 1:
               # time = user_dic['time']
              #  fist_time = fist_time + 1
            if int(time) >= 3:
                print('该账户重新输入密码超过三次已经被锁定，请联系管理员')
                #更新文件
                #print(name,pwd,time,id)
                target_file = ''
                for user_info_new in user_info_list:
                    name = user_info_new['name']
                    pwd = user_info_new['pwd']
                    time = user_info_new['time']
                    target = """%s|%s|%s\n""" %(name,pwd,time)
                    target_file =  target + target_file
                    #print(target)
                   # print(target_file)
                f2 = open('db', 'w')
                f2.write(target_file)
                f2.close()

                exit()
            if password == pwd:
                print("登录成功")
                time = 0
                # print(name, pwd, time, id)
                temp_user_dic={
                    'id': id,
                    'name': name,
                    'pwd': pwd,
                    'time': time
                }
                #重新写入字典
                user_info_list[id]= temp_user_dic
               # print(user_info_list)

                #更新文件
                target_file = ''
                for user_info_new in user_info_list:
                    name = user_info_new['name']
                    pwd = user_info_new['pwd']
                    time = user_info_new['time']
                    target = """%s|%s|%s\n""" %(name,pwd,time)
                    target_file =  target + target_file
                    #print(target)
                   # print(target_file)
                f2 = open('db', 'w')
                f2.write(target_file)
                f2.close()

                exit()
            else:
                #数据错误密码  更新time
                time = int(time) +1
                temp_user_dic={
                    'id': id,
                    'name': name,
                    'pwd': pwd,
                    'time': time
                }
                #重新写入字典
                user_info_list[id]= temp_user_dic
                break
    print('用户名或密码错误,请重新输入')
