#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# HAproxy配置文件操作
# 1. 根据用户输入输出对应的backend下的server信息
# 2. 可添加backend 和sever信息
# 3. 可修改backend 和sever信息
# 4. 可删除backend 和sever信息
# 5. 操作配置文件前进行备份
# 6 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作

# f = open('ha.conf', 'r', encoding='utf-8')
# for i in f:
#     print(i)
#     print('----')

#


def delete(backend, server_dict, option):
    # print(server_dict)
    server_list = []
    for i in server_dict:
        server_list.append(server_dict[i])
    # print(server_list)
    if option == 'a':  # 删除backend下所有内容
        if file_option(backend, server_list):
            server_list = []
            file_option(backend, server_list)
            print('删除完成。')
        else:
            print('删除失败。')
    elif option == 'r':
        print('输入新的backend名：')
        new_name = input().strip()
        print('确认将backend %s ,重命名为 backend %s么？y/n' %(backend, new_name))
        choose = input().strip()
        if choose == 'y':
            if file_option(backend, server_list, new_name):
                print('重命名完成。')
    else:
        # 检测用户输入是否正确
        try:
            # 用户输入去重复
            option_list = set(option.split(','))
            # print(option_list)
            for i in option_list:  # 检查输入是否为数字
                if not i.isdigit():
                    raise
        except:
            # 用户输入多余空格，字母等无效选项，则清空用户输入
            option_list = None
        if option_list:  # 用户输入正确
            flag = True
            delete_list = []
            for i in option_list:  # 检查输入各项是否正确
                i = int(i)
                if i >= len(server_list):  # 判断用户输入选项是否超出条目数
                    flag = False
                    print('没有这一条目：', i)
                else:
                    #  创建删除列表
                    delete_list.append(server_dict.get(i))
            if flag:
                print('即将删除'.center(35,'—'))
                for i in delete_list:
                    print(i)
                print(''.center(38, '—'))
                print('确认要删除这项项目?y/n :')
                c = input().strip()
                if c == 'y':
                    new_server_list = set(server_list).difference(set(delete_list))
                    file_option(backend, new_server_list)
                    print('成功删除', len(server_list)-len(new_server_list), '条')
                    print('new :backend %s'.center(35,'—') %backend)
                    for i in new_server_list:
                        print(i)
                    print(''.center(38, '—'))
                    return 'ok'
        else:
            print('输入有误，请按格式输入')


def add(*server_dict):

    add_list = []
    old_list = []
    if server_dict:
        server_dict = server_dict[0]
        for i in server_dict:
            old_list.append(server_dict[i])
        add_list += old_list
    flag = True

    # print('add_list:',add_list)
    count = 1
    print('完成请输入ok\n取消请输入q')
    while flag:
        flag1 = True
        new_server = input('请输入server%d:' % count).strip()
        new_server = new_server.split()
        new_server = ' '.join(new_server)  # 去除输入中多余的空格
        if new_server == '':
            continue
        if new_server == 'q':
            flag = False
            continue
        if new_server == 'ok':
            flag = False
        else:
            if new_server in add_list :
                print('已存在，请重新输入。')
                continue
            else:
                new_server_split = new_server.split()
                # print('new_server_split:', new_server_split)
                for i in add_list:
                    v = i.split()
                    if v == new_server_split:
                        new_server = []
                        print('已存在，请重新输入。')
                        flag1 = False
                        break
                    # print('v:', v)
                    if new_server_split[2] == v[2]:  # 判断ip是否存在
                        print('server_ip已存在，是否更新？y/n:')
                        o = input().strip()
                        if o == 'y':
                            add_list[add_list.index(i)] = new_server
                            count += 1
                            flag1 = False
                            break
                        else:
                            continue
                if flag1:
                    add_list.append(new_server)
                    count += 1
    if add_list:
        if file_option(backend, set(add_list)):
            print('更新成功')
        else:
            print('更新失败')
    else:
        print('无任何更新。')


def select(backend):
    server_list = []  # server查询结果存储列表
    # 打开文件进行处理
    with open('ha.conf', 'r', encoding='utf-8') as file_ha:
        flag = False
        for i in file_ha:  # 按行遍历内容
            # 查询到下一个backend 添加结束标记flag = False
            if flag and i.strip().startswith('backend'):
                flag = False
                continue
            # 查询到用户输入的backend 添加标记flag = True
            if i.strip().startswith('backend') and i.strip().endswith(backend):
                flag = True
            # 将标为True开始的下一行开始，至标记为False为止的每一行添加到server_list中
            if flag and i.strip().startswith('server'):
                server_list.append(i.strip())
    # print('共计条数：', len(server_list))
    # 将条目添加序号保存到字典中
    server_dict = dict(enumerate(server_list))
    # print(server_dict)
    # 显示查结果
    print('backend %s'.center(38, '—') %backend)
    print('序号|\tserver')
    print(''.center(35, '—'))
    for i in server_dict:
        print(i, '\t|\t', server_dict[i])
    return server_dict


def file_option(backend, server_list, *new_name):  # 接收两个参数，判断backend是否存在不存在则新建，存在则增加server
    # 备份至ha.conf.bak
    with open('ha.conf', 'r', encoding='utf-8') as f, open('ha.conf.bak', 'w', encoding='utf-8') as bak:
        for i in f:
            bak.write(i)
    with open('ha.conf.bak', 'r', encoding='utf-8') as old, open('ha.conf', 'w', encoding='utf-8') as new:
        flag = False
        flag1 = False
        b = []
        for i in old:
            if flag and i.strip().startswith('backend'):
                flag = False
                new.write(i)
                continue
            if i.strip().startswith('backend') and i.strip().endswith(backend):  # 判断backend是否存在
                flag = True
            if flag and i.strip().startswith('server'):
                b.append(i.strip())
            if not flag:
                new.write(i)
        if not server_list:
            return True
        else:
            if new_name:
                print(new_name)
                new.write('\nbackend ' + new_name[0])
                for i in server_list:
                    new.write('\n' + ' ' * 8 + i)
            else:
                new.write('\nbackend '+ backend)
                for i in server_list:
                    new.write('\n' + ' ' * 8 + i)
                return True

while True:

    backend = input('请输入需要操作的backend:').strip()
    # server = input('s:')
    if backend:
        server_dict = select(backend)
        # print(server_dict)
        if server_dict:
            while True:
                print('Menu'.center(37, '—'))
                print('|  (b)返回')
                print('|  (r)重命名')
                print('|  (i)添加server')
                print('|  (a)删除整个backend')
                print('|   删除server输入序号，以逗号分隔')
                print('|   例：1,3,5  （末尾不需要加逗号，请勿输入多余空格。')
                print(''.center(35, '—'))
                option = input().strip()
                if option == 'b':
                    break
                if option == 'i':
                    add(server_dict)
                else:
                    status = delete(backend, server_dict, option)
                    if status == 'ok':
                        break
        else:
            i = input('backend不存在，是否添加？y/n')
            if i == 'y':
                add()


    else:
        print('backend 不能为空。')
        # print('backend '+backend)




