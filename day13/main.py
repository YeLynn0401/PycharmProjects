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
def login():
    name = input('用户名：').strip()
    pwd = input('密 码：').strip()
    if name and pwd:
        data = session.query(sql_opt.User_info).filter_by(user_name=name).filter_by(user_pwd=pwd).first()
        if data:
            print('welcome', data.user_name)
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
    name = input('host：').strip()
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
    host = sql_opt.Server_info(server_name=name, server_ip=ip, server_key=key, server_pwd=pwd, server_port=port)
    session.add(host)
    session.commit()


def host_add_group():
    data = session.query(sql_opt.Group_info).filter_by().all()
    for i in data:
        print(i.id, i.name)
    print('请选择需要操作的组ID')
    group = input('ID：').strip()
    try:
        c = None
        if group.isdigit():
            for i in data:
                if i == group:
                    c = i
                    return c
        else:
            raise Exception('')
    except:
        print('输入有误')
    if c:
        pass
        # TODO

def user_add_group():
    pass

def create_group():
    name = input('name').strip()
    date = sql_opt.Group_info(group_name=name)
    session.add(date)
    session.commit()
    print('ok')






# login()
# date = session.query(sql_opt)
# host_add()
create_group()