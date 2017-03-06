#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import re
import table_opt
from sqlalchemy.orm import sessionmaker
import paramiko
import ssh_server

session_class = sessionmaker(bind=table_opt.engine)
session = session_class()


# user1 = table_opt.User_info(user_name='alex', user_pwd='123')
#
# session.add(user1)
#
# session.commit()
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
            return data.id, data.name
        else:
            print('用户名或密码错误。')
    else:
        print('用户名密码不能为空。')


def user_add():
    # 添加用户
    name = input('用户名：').strip()
    pwd = input('密 码：').strip()
    user1 = table_opt.User(name=name, pwd=pwd)
    try:
        session.add(user1)
        session.commit()
        print('ok')
    except:
        print('error')


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
    for i in group:
        print(i.id, i.name)
    print('请选择需要操作的组ID')
    # 选择要操作的组
    group_id = input('ID：').strip()
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
        print('none')


def user_add_group():
    # 查询组信息
    data = session.query(table_opt.Group_info).filter_by().all()
    if data:
        for i in data:
            print(i.id, i.group_name)
    print('请选择需要操作的组ID')
    # 选择要操作的组
    group = input('ID：').strip()
    c = cho(group, data)
    if c:
        host = session.query(table_opt.User_info).filter_by().all()
        # 打印主机列表
        if host:
            print('id,用户名')
            for i in host:
                print(i.id, i.user_name)
            h = input('ID').strip()
            choise = cho(h, host)
            if choise:
                obj1 = table_opt.User_group(user_id=int(choise), group_id=int(c))
                session.add(obj1)
                session.commit()
                print('添加成功')
            else:
                print('选择有误')


        else:
            print('请先添加用户')
    else:
        print('none')


def create_group():
    name = input('name').strip()
    date = table_opt.HostGroup(name=name)
    session.add(date)
    session.commit()
    print(date.id, date.name, 'ok')


def login_check(func):
    def wrapper(*args, **kwargs):
        if not user_id:
            print('请登录。')
            return
        s = func(*args, **kwargs)
        return s
    return wrapper


def add_host_user():
    name = input('用户名：').strip()
    pwd = input('密 码：').strip()
    key = input('key：').strip()
    if key:
        user1 = table_opt.HostUser(name=name, key=key)
    if pwd:
        user1 = table_opt.HostUser(name=name, pwd=pwd)
    try:
        session.add(user1)
        session.commit()
        print('ok')
    except:
        print('error')


def print_host_list(user_id):
    info_dict = {}
    data = session.query(table_opt.User).filter_by(id=user_id).first()
    for i in data.permission:
        print(i.host.name, )
    # for i in data.permission.host.name:
    #     # 格式化数据，去重复
    #     info_dict[i.host.ip] = [i.host.name, i]
    # for k in info_dict:
    #     print(k)
    # ip = input('请输入所选主机IP').strip()
    # try:
    #
    #     u = info_dict.get(ip)[1]
    #     users = u.m
    #     for i in users:
    #         print(i.id)
    #
    # except Exception as e:
    #     print('选择有误。')
    #     print(e)


@login_check
def test(a):
    print(a)

if __name__ == '__main__':
    user_id = None
    user_name = None
    while True:
        if user_id:
            print('1、{}：注销\n2、添加主机\n'
                  '3、创建主机组\n4、主机分组\n'
                  '5、用户分配主机\n6、添加跳板机用户\n'
                  '7、添加主机账户\n8、打印主机表'.format(user_name))
        else:
            print('1、登陆\n2、添加主机\n'
                  '3、创建主机组\n4、主机分组\n'
                  '5、用户分配主机\n6、添加跳板机用户\n'
                  '7、添加主机账户\n8、打印主机表'.format(user_name))
        user_input = input('').strip()
        if user_input == '1':
            if user_id:  # 注销
                user_id = None
                user_name = None
                continue
            ret = login()
            if ret:
                user_id, user_name = ret

        # date = session.query(table_opt)
        elif user_input == '2':
            host_add()
        elif user_input == '3':
            create_group()
        elif user_input == '4':
            host_add_group()
        elif user_input == '5':
            user_add_group()
        elif user_input == '6':
            user_add()
        elif user_input == '7':
            add_host_user()
            # data = session.query('host').filter_by(id=1).first()
            # data.groups= []
        elif user_input == '8':
            print_host_list(user_id)
        elif user_input == '9':
            conn = ssh_server.conn(user_name)
            conn()
