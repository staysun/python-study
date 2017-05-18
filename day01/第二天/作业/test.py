#!/usr/bin/python
# -*- coding:utf-8 -*-

def get_user_data():
    # 读取user 数据
    f1 = open('user', 'r')
    user_data = f1.read()
    f1.close()

    # 初始化用户数据
    user_info_list = []
    user_str_list = user_data.split('\n')

    user_id = 0
    # 格式化 用户数据
    for i in user_str_list:
        if i == '':
            break
        temp = i.split('|')
        # print(temp)
        v = {
            'user_id': user_id,
            'user_name': temp[0],
            'user_pwd': temp[1],
            'user_time': temp[2],
            'user_money': temp[3]

        }
        user_id = user_id + 1
        user_info_list.append(v)
    return  user_info_list



def get_gouwuche_data():
    f3 = open('gouwuche', 'r', encoding='utf-8')
    gouwuche_data = f3.read()
    f3.close()

    # 初始化 购物车数据
    gouwuche_dic = {}
    gouwuche_str_list = gouwuche_data.split('\n')

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
    return  gouwuche_dic


def get_shangpin_data():
    # 读取商品
    f2 = open('shangpin', 'r', encoding='utf-8')
    shangpin_data = f2.read()
    f2.close()

    # 初始化 商品数据
    shangpin_list = []
    shangpin_str_list = shangpin_data.split('\n')

    id_shangpin = 0
    # 格式化 商品数据
    for i in shangpin_str_list:
        if i == '':
            break
        temp = i.split('|')
        # print(temp)
        v = {
            'id': id_shangpin,
            'shangpin_name': temp[0],
            'shangpin_money': temp[1]
        }
        id_shangpin = id_shangpin + 1
        shangpin_list.append(v)

    return shangpin_list



def select_dir():
    title = '选择'
    chose = title.center(40, '#')
    commodity= '1 >>商品列表'
    gouwuche = '2 >>购物车'
    qxit_name = '3 >>退出程序'
    chose_title = title.center(40, '#')
    commodity_title = commodity.center(40, '#')
    gouwuche_title = gouwuche.center(40, '#')
    qxit_name_title = qxit_name.center(40, '#')

    print(chose_title)
    print(commodity_title)
    print(gouwuche_title)
    print(qxit_name_title)
    seq_no = input('请输入选择的序号:')
    shangpin_list = get_shangpin_data()
    if seq_no == '1':
        for shangpin_item in  shangpin_list:
            print('#####','id:',shangpin_item['id'],'>>>','商品名称：',shangpin_item['shangpin_name'],'#### 商品价格：',shangpin_item['shangpin_money'])

        into_gouwuche=input('请输入需要购买的商品id :')

        gouwuche_dic = get_gouwuche_data()
        print(gouwuche_dic)




def user_login():
    while True:
        input_user_name = input('请输入用户名:')
        input_password = input('请输入密码:')
        user_info_list = get_user_data()
        # print(user_name,password)
        ##判断是否为空
        if input_user_name == '' or input_password == '':
            print('用户名或密码不能为空')
            continue
        for i in user_info_list:
            if input_user_name == i['user_name']:
                print('登录成功')
                select_dir()
        print('用户名密码错误')




user_login()
