#!/usr/bin/python
# -*- coding:utf-8 -*-



def get_data():
    #读取user 数据
    f1 = open('user','r')
    user_data = f1.read()
    f1.close()

    #初始化用户数据
    user_info_list = []
    user_str_list = user_data.split('\n')


    #读取商品
    f2 = open('shangpin','r',encoding= 'utf-8')
    shangpin_data = f2.read()
    f2.close()

    #初始化 商品数据
    shangpin_list = []
    shangpin_str_list = shangpin_data.split('\n')


    ##读取购物车
    f3 =  open('gouwuche','r',encoding= 'utf-8')
    gouwuche_data = f3.read()
    f3.close()

    #初始化 购物车数据
    gouwuche_dic ={}
    gouwuche_str_list = gouwuche_data.split('\n')


    ##读取购物车数据

    gouwuche_id = 0

    for i in  gouwuche_str_list:
        if i == '':
            break
        temp = i.split('|')
        # print(temp)
        temp_shangpin_name =temp[1].split('，')
        # print(temp_shangpin_name)
        v = {
            # 'user_name': temp[0],
             temp[0]:temp_shangpin_name
        }
        gouwuche_dic.update(v)
        #print(gouwuche_dic)





    id_shangpin = 0
    #格式化 商品数据
    for i in shangpin_str_list:
        if i == '':
            break
        temp = i.split('|')
        # print(temp)
        v = {
            'id': id_shangpin,
            'shangpin_name': temp[0],
             'shangpin_money':temp[1]
        }
        id_shangpin = id_shangpin + 1
        shangpin_list.append(v)

    #print(shangpin_list)



    user_id = 0
    #格式化 用户数据
    for i in user_str_list:
        if i == '':
            break
        temp = i.split('|')
        # print(temp)
        v = {
            'user_id': user_id,
            'user_name': temp[0],
             'user_pwd':temp[1],
            'user_time':temp[2],
            'user_money':temp[3]

        }
        user_id = user_id + 1
        user_info_list.append(v)
        print(user_info_list)



def user_login():
    while True:
        ##输入用户名密码
        input_user_name = input('请输入用户名:')
        input_password = input('请输入密码:')
        # print(user_name,password)
        ##判断是否为空
        if input_user_name == '' or input_password == '':
            print('用户名或密码不能为空')
        get_data()






user_login()


#
#     while True:
#         ##输入用户名密码
#         title = '登录'
#         login_title = title.center(40, '#')
#         print(login_title)
#         user_name = input('请输入用户名:')
#         password = input('请输入密码:')
#         # print(user_name,password)
#         ##判断是否为空
#         if user_name == '' or password == '':
#             print('用户名或密码不能为空')
#             continue
#         # 获取用户名密码
#         # print(user_info_list)
#         for user_dic in user_info_list:
#             name = user_dic['name']
#             pwd = user_dic['pwd']
#             time = user_dic['time']
#             id = user_dic['id']
#             money = user_dic['money']
#
#             # if fist_time == 1 :
#             #     time = user_dic['time']
#             # fist_time = fist_time + 1
#             # 判断登录规则
#             if user_name == name:
#                 print('登录成功')
#                 title = '选择'
#                 chose = title.center(40, '#')
#                 commodity= '1 >>商品列表'
#                 gouwuche = '2 >>购物车'
#                 qxit_name = '3 >>退出程序'
#                 chose_title = title.center(40, '#')
#                 commodity_title = commodity.center(40, '#')
#                 gouwuche_title = gouwuche.center(40, '#')
#                 qxit_name_title = qxit_name.center(40, '#')
#
#                 print(chose_title)
#                 print(commodity_title)
#                 print(gouwuche_title)
#                 print(qxit_name_title)
#                 seq_no = input('请输入选择的序号:')
#                 if seq_no == '1':
#                     for shangpin_item in  shangpin_list:
#                         print('#####','id:',shangpin_item['id'],'>>>','商品名称：',shangpin_item['shangpin_name'],'#### 商品价格：',shangpin_item['shangpin_money'])
#
#                     into_gouwuche=input('请输入需要购买的商品id')
#                     for shangpin_item in shangpin_list:
#                         shangpin_id = shangpin_item['id']
#                         shangpin_id =str(shangpin_id)
#                         shangpin_name = shangpin_item['shangpin_name']
#                         shangpin_money = shangpin_item['shangpin_money']
#                         if shangpin_id == into_gouwuche:
#                              surplus = int(money)- int(shangpin_money)
#                              if surplus > 0:
#                                 gouwuche_dic[user_name].append(shangpin_name)
#                                 print('余额为',surplus)
#                              else:
#                                  print('您的钱不足')
#                                 #gouwuche_list[user_name]
#
#                 elif seq_no == '2':
#                     print('购物车')
#                 elif seq_no == '3':
#                     exit()
#                 else:
#                     print('输入错误重新输入')
#
#
#             else:
#                 print('请输入正确的用户名密码')
#
# get_data()