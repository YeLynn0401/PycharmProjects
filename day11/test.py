#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
localIP = socket.gethostbyname(socket.gethostname())#这个得到本地ip
print("local ip:%s "%localIP)
ipList = socket.gethostbyname_ex(socket.gethostname())
for i in ipList:
    if i != localIP:
       print("external IP:%s"%i)