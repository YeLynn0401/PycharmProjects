#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import sql_opt
from sqlalchemy.orm import sessionmaker
import paramiko

session_class = sessionmaker(bind=sql_opt.engine)
session = session_class()


# user1 = sql_opt.User_info(user_name='alex', user_pwd='123')
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
        data = session.query(sql_opt.User_info).filter_by(user_name=name).filter_by(user_pwd=pwd).first()
        if data:
            print('welcome', data.user_name)
            return data.id, data.user_name
        else:
            print('用户名或密码错误。')
    else:
        print('用户名密码不能为空。')


def user_add():
    name = input('用户名：').strip()
    pwd = input('密 码：').strip()
    user1 = sql_opt.User_info(user_name=name, user_pwd=pwd)
    try:
        session.add(user1)
        session.commit()
        print('ok')
    except:
        print('error')


def host_add():
    name = input('user_name：').strip()
    port = input('port：').strip()
    pwd = input('pwd：').strip()
    ip = input('ip ：').strip()
    key = input('key ：').strip()
    # s = paramiko.SSHClient()
    # if key:
    #     hkey = paramiko.RSAKey.from_private_key_file(key)
    #     s.load_system_host_keys()
    #     s.connect(name, port, 'root', pkey=key)
    # else:
    #     stdin, stdout, stderr = s.exec_command('hostname')
    #     print(stdout.read())
    ret  = ssh_conn(ip, int(port), name, pwd)
    if ret:
        print(ret)
        host = sql_opt.Server_info(server_name=ret, server_ip=ip, server_key=key, server_pwd=pwd, server_port=port)
        session.add(host)
        session.commit()
        print('添加成功')
    else:
        print('信息有误')


def host_add_group():  # 主机分组
    # 查询组信息
    data = session.query(sql_opt.Group_info).filter_by().all()
    for i in data:
        print(i.id, i.group_name)
    if not data:
        print('请先添加分组')
        return
    print('请选择需要操作的组ID')
    # 选择要操作的组
    group = input('ID：').strip()
    c = cho(group, data)
    if c:
        host = session.query(sql_opt.Server_info).filter_by().all()
        # 打印主机列表
        if host:
            print('id,主机名，ip')
            for i in host:
                print(i.id, i.server_name, i.server_ip)
            h = input('ID').strip()
            choise = cho(h, host)
            if choise:
                obj1 = sql_opt.Server_group(server_id=int(choise), group_id=int(c))
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
    data = session.query(sql_opt.Group_info).filter_by().all()
    if data:
        for i in data:
            print(i.id, i.group_name)
    print('请选择需要操作的组ID')
    # 选择要操作的组
    group = input('ID：').strip()
    c = cho(group, data)
    if c:
        host = session.query(sql_opt.User_info).filter_by().all()
        # 打印主机列表
        if host:
            print('id,用户名')
            for i in host:
                print(i.id, i.user_name)
            h = input('ID').strip()
            choise = cho(h, host)
            if choise:
                obj1 = sql_opt.User_group(user_id=int(choise), group_id=int(c))
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
    date = sql_opt.Group_info(group_name=name)
    session.add(date)
    session.commit()
    print('ok')


def login_check(func):
    def wrapper(*wargs, **kwargs):
        if not user_id:
            print('请登录。')
            return
        s = func(*wargs, **kwargs)
        return s
    return wrapper


@login_check
def test(a):
    print(a)

if __name__ == '__main__':
    user_id = None
    user_name = None
    while True:
        if user_id:
            print('1、{}：注销\n2、添加主机\n3、创建主机组\n4、主机分组\n5、用户分组\n6、添加用户'.format(user_name))
        else:
            print('1、登陆\n2、添加主机\n3、创建主机组\n4、主机分组\n5、用户分组\n6、添加用户'.format(user_name))
        user_input = input('').strip()
        if user_input == '1':
            if user_id:  # 注销
                user_id = None
                user_name = None
                continue
            ret = login()
            if ret:
                user_id, user_name = ret

        # date = session.query(sql_opt)
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
            test('asf')