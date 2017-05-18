#!/usr/bin/python
# -*- coding:utf-8 -*-



def get_file():
    '''获取数据文件'''
    f = open('emp','r',encoding='utf-8')
    data = f.read()
    return  data
def show_tables():
    """可以查询有哪些表"""
    print('+---------------------------+')
    print('| Tables_in_staysql         |')
    print('+---------------------------+')
    print('| emp                       |')
    print('+---------------------------+')



def desc():
    """查询表结构"""
    table_cloumn = create_table()
    print('+----------------+')
    print('| Column_Name    |')
    print('+----------------+')
    for i in table_cloumn:
        v= "|"+ i.ljust(16) + "|"
        print(v)
    print('+----------------+')


def create_table():
    """定义表结构 为以后判断做准备"""
    table_cloum=['ID','NAME','AGE','PHONE','DEPT','ENROLL_DATE']
    return  table_cloum




def  treating_cloum_data(cloum_data):
    '''处理select 过来的列名字  返回对应的数据的列的序号'''
    select_cloum_name_list = cloum_data[0].split(',')
#    print(select_cloum_name_list)
    cloum_data_seq_list =[]
    for cloum_name in select_cloum_name_list:
        if cloum_name not in create_table():
            sql_type =1
            return sql_type
        else:
            select_cloum_seq =create_table().index(cloum_name)
            # print(select_cloum_seq)
            cloum_data_seq_list.append(select_cloum_seq)
    # print(cloum_data_seq_list)
    return cloum_data_seq_list


def select(sql):
    """查询语句"""
    #检查 sql 语句是否正确
    try:
        #from 判断表的名字
        from_index =sql.index('FROM')
        table_index = from_index + 1
        table_name = sql[table_index]
        if table_name != 'EMP;' and  table_name != 'EMP' :
            sql_type = 1
            return sql_type
        file_data = get_file()
        select_cloum_name = sql[1:from_index]
        #处理 字段为*
        # if select_cloum_name == ['*']:
        #     for i in create_table():
        #         print(i,end=',')
        #     print('')
        #     print(file_data)
        #     return 0
        #处理字段 不是*的
        # select_cloum_seq_list = treating_cloum_data(select_cloum_name)
        # print(select_cloum_name[0])
        # for line in get_file().split():
        #     line_list = line.split(',')
        #     for i in select_cloum_seq_list:
        #         print(line_list[i],end=',')
        #     print('')
        #     #print(line_list)
        # where_index = sql.index('WHERE')
        # print(sql[where_index,-1])

        # print(get_file().split())
        # print(select_cloum_seq_list)

    except:
        print("ERR: 语法错误请检查")

    #处理字段 不是*的
    try:
        select_cloum_seq_list = treating_cloum_data(select_cloum_name)
        where_index = sql.index('WHERE')
        #print(where_index)
        #print(sql[where_index+1:])
        and_count = sql.count('AND')
        or_count =sql.count('OR')
        in_count =sql.count('IN')
        where_count=sql.count('AND') +sql.count('OR') + sql.count('IN')

        if where_count == 0:
            where_name = sql[where_index+1]
            where_condition = sql[where_index+2]
            where_valuse = sql[where_index+3].strip(';')
            # print(where_name,where_condition,where_valuse)
            if where_name not in create_table() or where_condition not in ['=','>','<']:
                return 1

            select_cloum_seq_list = treating_cloum_data(select_cloum_name)
            #打印表头
            if select_cloum_name == ['*']:
                for i in create_table():
                    print(i,end=',')
                print()
            else:
                print(select_cloum_name[0])
            # if where_condition == '=':
            for line in get_file().split():
                line_list = line.split(',')
                cloum_valuse = line_list[create_table().index(where_name)]
                ##找出来  where_valuse 对应的字典的位置  然后取 出数据对比   看是否正确  正确打印
                if where_condition == '=':
                    if cloum_valuse == where_valuse:
                        if select_cloum_name == ['*']:
                            print(line)
                        else:
                            for i in select_cloum_seq_list:
                                #print(select_cloum_seq_list)
                                print(line_list[i], end=',')
                        print('')
                elif where_condition == '>':
                    if line[create_table().index(where_name)] > where_valuse:
                        if select_cloum_name == ['*']:
                            print(line)
                        else:
                            for i in select_cloum_seq_list:
                                print(line_list[i], end=',')
                            print('')
                elif where_condition == '<':
                    if line[create_table().index(where_name)] < where_valuse:
                        if select_cloum_name == ['*']:
                            print(line)
                        else:
                            for i in select_cloum_seq_list:
                                print(line_list[i], end=',')
                            print('')


    except:
        select_cloum_seq_list = treating_cloum_data(select_cloum_name)
        #print(select_cloum_seq_list)
        # print(select_cloum_name[0])
        if select_cloum_name == ['*']:
            for i in create_table():
                print(i, end=',')
            print()
        else:
            print(select_cloum_name[0])
        for line in get_file().split():
            line_list = line.split(',')
            if select_cloum_name == ['*']:
                print(line)
            else:
                for i in select_cloum_seq_list:
                    #print(i)
                    print(line_list[i], end=',')
                print('')

def update(sql):
    """查询语句"""
    print(sql)
    update_valuses_dic ={}
    if sql[1] != 'EMP' or sql[2] != 'SET':
        return  1


    try:
        where_index = sql.index('WHERE')

    except:
        where_index = 0
    if sql[4] == '=':
        update_cloum = sql[3]
        update_value = sql[5]
        update_valuses_dic .update({update_cloum:update_value})
    else:
        update_valuses_list = sql[3].split(',')
        for i in update_valuses_list:
            update_cloum = i.split('=')[0]
            update_value = i.split('=')[1]
            update_valuses_dic.update({update_cloum: update_value})

    if where_index > 0 :
        update_where_cloum = sql[where_index+1]
        update_where_condition = sql[where_index+2]
        update_where_value = sql[where_index+3].strip(';')
        if update_where_cloum not in create_table() or update_where_condition not in ['=', '>', '<']:
            return 1
        line_data = ''
        for line in get_file().split():
            line_list = line.split(',')
            cloum_valuse = line_list[create_table().index(update_where_cloum)]
            if update_where_cloum == 'ID':
                cloum_valuse = int(cloum_valuse)
                update_where_value = int(update_where_value)
            if update_where_condition == '=':
                if cloum_valuse == update_where_value:
                    for cloum_name in update_valuses_dic:
                            cloum_index = create_table().index(cloum_name)
                            line_list.pop(cloum_index)
                            line_list.insert(cloum_index,update_valuses_dic[cloum_name])
                    #print(line_list)
                    update_line =''
                    for i in line_list:
                        update_line = update_line +',' + i
                    #print(update_line.strip(','))
                    line_data = line_data +'\n'+ update_line.strip(',')
                else:
                    line_data = line_data +'\n' + line
                    #print(line)
                    #print()
                    # for cloum_name in update_valuses_dic:
                    #     print(line,update_valuses_dic)

            elif update_where_condition == '>':
                if cloum_valuse > update_where_value:
                    for cloum_name in update_valuses_dic:
                            cloum_index = create_table().index(cloum_name)
                            line_list.pop(cloum_index)
                            line_list.insert(cloum_index,update_valuses_dic[cloum_name])
                    #print(line_list)
                    update_line =''
                    for i in line_list:
                        update_line = update_line +',' + i
                    #print(update_line.strip(','))
                    line_data = line_data +'\n'+ update_line.strip(',')
                else:
                    line_data = line_data +'\n' + line
                    #print(line)
                    #print()
                    # for cloum_name in update_valuses_dic:
                    #     print(line,update_valuses_dic)
            elif update_where_condition == '<':
                if cloum_valuse < update_where_value:
                    for cloum_name in update_valuses_dic:
                            cloum_index = create_table().index(cloum_name)
                            line_list.pop(cloum_index)
                            line_list.insert(cloum_index,update_valuses_dic[cloum_name])
                    update_line =''
                    for i in line_list:
                        update_line = update_line +',' + i
                    line_data = line_data +'\n'+ update_line.strip(',')
                else:
                    line_data = line_data +'\n' + line

    if where_index == 0:
        line_data = ''
        for line in get_file().split():
            line_list = line.split(',')
            for cloum_name in update_valuses_dic:
                cloum_index = create_table().index(cloum_name)
                line_list.pop(cloum_index)
                line_list.insert(cloum_index, update_valuses_dic[cloum_name])
                # print(line_list)
                update_line = ''
            for i in line_list:
                update_line = update_line + ',' + i
                    # print(update_line.strip(','))
            line_data = line_data + '\n' + update_line.strip(',')



    with open('emp',mode='w',encoding='utf-8') as delete_f:
        delete_f.write(line_data)




def delete(sql):
    """删除数据库数据"""
    global delete_data
    if sql[1] != 'EMP':
        return  1

    try:
        where_index = sql.index('WHERE')
        detele_where_cloum_name = sql[where_index+1]
        detele_where_condition = sql[where_index+2]
        detele_where_values = sql[where_index + 3].strip(';')
        #print(detele_where_cloum_name,detele_where_condition,detele_where_values )

        if detele_where_cloum_name not in create_table() or detele_where_condition not in ['=', '>', '<']:
            return 1
        select_cloum_seq_list = treating_cloum_data(detele_where_cloum_name)
        delete_data = ''

        for line in get_file().split():
            line_list = line.split(',')
            cloum_valuse = line_list[create_table().index(detele_where_cloum_name)]
            #print(cloum_valuse)
            ##找出来  where_valuse 对应的字典的位置  然后取 出数据对比   看是否正确  正确打印

            if detele_where_cloum_name == 'ID':
                cloum_valuse = int(cloum_valuse)
                detele_where_values = int(detele_where_values)

            if detele_where_condition == '=':
                if cloum_valuse == detele_where_values:
                    pass
                else:
                    delete_data = delete_data + '\n' + line
                # print(delete_data)
            elif detele_where_condition == '>':
                if cloum_valuse> detele_where_values:
                    pass
                else:
                    delete_data = delete_data + '\n' + line
            elif detele_where_condition == '<':
                if cloum_valuse < detele_where_values:
                    pass
                else:
                    delete_data = delete_data + '\n' + line
        with open('emp', mode='w', encoding='utf-8') as delete_f:
            delete_f.write(delete_data)
        print('delete 成功')


    except:
        print('删除emp表所有数据')
        with open('emp',mode='w',encoding='utf-8') as delete_f:
            pass

    #print(sql)

def insert(sql):
    """增加记录"""
    ###获取id  自增
    if sql[1] != 'INTO' or sql[2] != 'EMP' :
        print('ERR ：   语法错误')
        return 1

    emp_seq = 0
    for line in get_file().split():
        line_list = line.split(',')
        number = int(line_list[0])
        if number > emp_seq:
            emp_seq = number

    ###获取 语句中的数据
    #print(sql[3][7:-1])
    insert_data = '\n' + str(emp_seq+1) +',' + sql[3][7:-1]
    with open('emp',mode='a',encoding='utf-8') as insert_f:
        insert_f.write(insert_data)
    print('insert 成功')


def help():
    """帮助信息"""
    print("目前支持的语句为")
    print("help                   查看帮助信息")
    print("show tabes;            查看目前的表信息")
    print("desc [table_name];      查看表的结构")
    print('''selct [Column_Name] from [table_name] where [Column_Name] [>< =] [变量];      查询数据
            例： select id,name from emp where id = 1 ; 条件必须 有空格 不能是 id=1； ''')
    print("insert into table_name values(str) ;     查询数据")
    print("""delete table_name where cloum_name = values  删除数据
            不能 使用 cloum_name=values""")
    print("""update :支持下列写法
        # update emp set name = 张旭 where id = 1 ;
        # update emp set name=张旭,dept=db where id = 1 ;""")
    print("q                      退出staysql")




# def clean_sql(sql):
#     """清洗sql"""
#     sql_clean = sql.strip()
#     if sql_clean.endswith(';') or sql_clean.endswith('\g') or sql_clean.endswith('\G'):
#         pass
#     else:
#         print("ERR: 000001 sql 语句必须已 ;或者\g 结尾")
#     print(sql_clean)



def main():
    """执行后计入登录提示"""
    print("欢迎登录staysql 数据库系统,请以;或\g 结尾")
    print("可以选择输入help 查看帮助信息")
    while True:
        sql = input("staysql >").strip().upper()
        sql = sql.split()
        #print(sql)
        if sql ==['Q'] or sql == ['Q',';'] or sql ==['Q;']:
            exit()
        elif sql == ['DESC', 'EMP;'] or sql == ['DESC', 'EMP',';'] or  sql == ['DESC', 'EMP'] :
            desc()
        elif sql == ['HELP'] or sql == ['HELP',';'] or sql == ['HELP;']:
            help()
        elif sql == ['SHOW', 'TABLES;'] or sql == ['SHOW', 'TABLES',';'] or sql == ['SHOW', 'TABLES',';']:
            show_tables()
        elif sql[0] == 'INSERT':
            insert(sql)
        elif sql[0] == 'UPDATE':
            sql_type = update(sql)
            if sql_type == 1:
                print('ERR: 语法错误请检查 您可以选择输入help 帮助')
        elif sql[0] == 'DELETE':
            sql_type = delete(sql)
            if sql_type == 1:
                print('ERR: 语法错误请检查 您可以选择输入help 帮助')
        elif sql[0] == 'SELECT':
            sql_type =select(sql)
            if sql_type == 1:
                print('ERR: 语法错误请检查 您可以选择输入help 帮助')
        else:
            print("sql 输入错误 您可以选择输入help 帮助")


main()


