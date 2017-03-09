#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import re

from sqlalchemy.orm import sessionmaker
import paramiko
import ssh_server
import logging
import sys
try:
    import table_opt
except:
    print('连接数据库失败,请检查服务器状态。')
    sys.exit(0)

session_class = sessionmaker(bind=table_opt.engine)
session = session_class()


def ssh_conn(host, port, username, pwd):
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname=host, port=port, username=username, password=pwd)
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command('hostname')

    # 获取命令结果
    out = stdout.read().decode()
    err = stderr.read().decode()
    ssh.close()
    if out:
        return out
    # 关闭连接


def cho(inp, data):
    c = None
    try:
        if inp.isdigit():
            inp = int(inp)
            for i in data:
                if i.id == inp:
                    c = i.id
                    return c
        else:
            raise Exception('输入有误')
    except:
        print('输入有误')


def login():
    name = input('用户名：').strip()
    pwd = input('密 码：').strip()
    if name and pwd:
        data = session.query(table_opt.User).filter_by(name=name).filter_by(pwd=pwd).first()
        if data:
            print('welcome', data.name)
            logging.info('{} login success'.format(data.name))
            return data.id, data.name
        else:
            print('用户名或密码错误。')
            logging.warning('{} login err'.format(name))
    else:
        print('用户名密码不能为空。')


def user_add():
    # 添加跳板机用户
    name = input('用户名：').strip()
    pwd = input('密 码：').strip()
    if name and pwd:
        user1 = table_opt.User(name=name, pwd=pwd)
        try:
            session.add(user1)
            session.commit()
            print('ok')
        except:
            print('error')
    else:
        print('用户名密码不能为空')


def host_add():
    # 添加主机
    name = input('server_name：').strip()
    port = input('port：').strip()
    ip = input('ip ：').strip()
    # s = paramiko.SSHClient()
    # if key:
    #     hkey = paramiko.RSAKey.from_private_key_file(key)
    #     s.load_system_host_keys()
    #     s.connect(name, port, 'root', pkey=key)
    # else:
    #     stdin, stdout, stderr = s.exec_command('hostname')
    #     print(stdout.read())
    if name and ip:

        r = re.match('^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$', ip)
        if not r:
            print('ip输入有误')
            return
        if port:
            if port.isdigit():
                host = table_opt.Host(name=name, ip=ip, port=int(port))
            else:
                print('端口为整数')
                return
        else:
            host = table_opt.Host(name=name, ip=ip)

        try:
            session.add(host)
            session.commit()
            print(ip, '添加成功')
        except Exception as e:
            print('服务器已存在，添加失败')
    else:
        print('服务器名和IP不能为空')


def host_add_group():  # 主机分组
    # 查询组信息
    group = session.query(table_opt.HostGroup).filter_by().all()
    # for i in group:
    #     print(i.id, i.group_name)

    if not group:
        print('请先添加分组')
        return
    print('id，组名')
    for i in group:
        print(i.id, i.name)
    print('请选择需要操作的组ID')
    # 选择要操作的组
    group_id = input('请输入主机ID：').strip()
    c = cho(group_id, group)
    if c:
        host = session.query(table_opt.Host).filter_by().all()
        # 打印主机列表
        if host:
            print('id,主机名，ip')
            for i in host:
                print(i.id, i.name, i.ip)
            h = input('ID').strip()
            choise = cho(h, host)
            if choise:
                obj1 = table_opt.Host_m2m_HostGroup(host_id=int(choise), group_id=int(c))
                session.add(obj1)
                session.commit()
                print('添加成功')
            else:
                print('选择有误')


        else:
            print('请先添加主机')
    else:
        print('输入有误')


def user_add_host():
    # 跳板机用户分配主机

    hosts = session.query(table_opt.Host_m2m_Hostuser).all()
    if not hosts:
        print('还没有可用主机')
        return
    hosts_list = list(enumerate(hosts))
    for i in hosts_list:
        print(i[0], i[1].host.ip, i[1].host.name, i[1].hostuser.name)
    c = input('请输入序号').strip()
    try:
        host_m2m_hostuser_id = hosts_list[int(c)][1].id
        users = session.query(table_opt.User).all()
        users_list = list(enumerate(users))
        if not users_list:
            print('还没有添加跳板机用户。')
            return
        print('id', '用户名')
        for u in users_list:
            print(u[0], u[1].name)
        user = input('请选择id：').strip()
        us_id = users_list[int(user)][1].id
        host = table_opt.UserPermission(user_id=us_id, host_m2m_hostuser_id=host_m2m_hostuser_id)
        session.add(host)
        session.commit()
        print('添加成功')
    except Exception as e:
        print(e)
        print('选择有误')
    # c = cho(group, data)
    # if c:
    #     host = session.query(table_opt.User_info).filter_by().all()
    #     # 打印主机列表
    #     if host:
    #         print('id,用户名')
    #         for i in host:
    #             print(i.id, i.user_name)
    #         h = input('ID').strip()
    #         choise = cho(h, host)
    #         if choise:
    #             obj1 = table_opt.User_group(user_id=int(choise), group_id=int(c))
    #             session.add(obj1)
    #             session.commit()
    #             print('添加成功')
    #         else:
    #             print('选择有误')
    #
    #
    #     else:
    #         print('请先添加用户')
    # else:
    #     print('none')


def create_group():
    # 创建主机组
    name = input('name').strip()
    date = table_opt.HostGroup(name=name)
    session.add(date)
    session.commit()
    # print(date.id, date.name, 'ok')


def login_check(func):
    def wrapper(*args, **kwargs):
        if not user_id:
            print('请登录。')
            return
        s = func(*args, **kwargs)
        return s
    return wrapper


def add_host_user():
    # 添加服务器用户和密码
    name = input('用户名：').strip()
    pwd = input('密 码：').strip()
    key = input('key：').strip()
    if not name:
        print('用户名不能为空')
    if key or pwd:
        user1 = table_opt.HostUser(name=name,pwd=pwd, key=key)
    else:
        print('密码或者key必须填一个')
        return
    try:
        session.add(user1)
        session.commit()
        print('ok')
    except:
        print('error')


def print_host_list(user_id, user_name):
    # 跳板机用户登陆有限权主机
    info_dict = {}
    data = session.query(table_opt.User).filter_by(id=user_id).first()
    if not data.permission:
        print('还没有任何权限，请联系管理员')
        return 'q'
    tem = list(enumerate(data.permission))
    print('id, 主机名，ip， 用户名')
    for i in tem:
        print(i[0], i[1].host.name, i[1].host.ip, i[1].hostuser.name)
    ids = input('请选择要连接的主机id:').strip()
    if ids == 'q':
        # 输入q 退出
        return 'q'
    if ids.isdigit():
        ids = int(ids)
    else:
        print('输入有误')
    try:
        print(tem[ids][1].host.ip, tem[ids][1].host.port, tem[ids][1].hostuser.name, tem[ids][1].hostuser.pwd, tem[ids][1].hostuser.key)
        connn = ssh_server.conn(user_name, tem[ids][1].host.ip, tem[ids][1].host.port, tem[ids][1].hostuser.name, tem[ids][1].hostuser.pwd, tem[ids][1].hostuser.key)
        connn()
    except:
        print('bye...')


def host_config_user():
    # 主机配置用户名
    hosts = session.query(table_opt.Host).all()
    if not hosts:
        print('还没有主机')
        return
    hosts_list = list(enumerate(hosts))
    print('id，主机名，IP')
    for i in hosts_list:
        print(i[0], i[1].name, i[1].ip)
    c = input('选择主机id').strip()
    try:
        host_id = hosts_list[int(c)][1].id
        hostusers= session.query(table_opt.HostUser).all()
        if not hostusers:
            print('还没有添加用户')
            return
        hostusers_list = list(enumerate(hostusers))
        print('id，用户名，密码，key')
        for i in hostusers_list:
            print(i[0], i[1].name, i[1].pwd, i[1].key)
        c = input('选择用户名id').strip()
        hostuser_id = hostusers_list[int(c)][1].id
        obj = table_opt.Host_m2m_Hostuser(host_id=host_id, hostuser_id=hostuser_id)
        session.add(obj)
        session.commit()
        print('添加成功。')
    except Exception as e:
        print(e)
        print('添加失败')



@login_check
def test(a):
    print(a)

if __name__ == '__main__':
    # 配置log信息
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='logs/login.log',
                        filemode='a')
    while True:
        x = input('1、管理员选项\n2、用户登陆\n:').strip()
        if x == '1':
            while True:
                print('1、添加主机\n'
                      '2、创建主机组\n3、主机关联主机组\n'
                      '4、跳板机用户关联主机\n5、添加跳板机用户\n'
                      '6、添加服务器账户\n7、主机关联用户名')

                user_input = input('').strip()
                # if user_input == '1':
                #     if user_id:  # 注销
                #         user_id = None
                #         user_name = None
                #         continue
                #     ret = login()
                #     if ret:
                #         user_id, user_name = ret
                if user_input == '1':
                    host_add()
                elif user_input == '2':
                    create_group()
                elif user_input == '3':
                    host_add_group()
                elif user_input == '4':
                    user_add_host()
                elif user_input == '5':
                    user_add()
                elif user_input == '6':
                    add_host_user()
                elif user_input == '7':
                    host_config_user()
                elif user_input == 'q':
                    break

        elif x == '2':
            # 用户id
            user_id = None
            # 用户姓名
            user_name = None
            ret = login()
            if ret:
                user_id, user_name = ret
                while True:
                    result = print_host_list(user_id, user_name)
                    if result == 'q':
                        break