#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import redis

r = redis.Redis(host='192.168.100.5')
r.set('foo', 'Bar')
print(r.get('foo'))