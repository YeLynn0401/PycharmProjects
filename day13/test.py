#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.100.5', port=22, username='root', password='123456')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('asdas')
# 获取命令结果

out = stdout.read().decode()
err = stderr.read().decode()
ssh.close()
if out:
    print(out)
else:
    print(err)

# 关闭连接

