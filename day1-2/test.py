#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


def fetch(backend):
    # backend == "www.oldboy.org"
    result = []
    with open('ha.conf','r',encoding='utf-8') as f:
        flag = False
        for line in f:
            print("backend" + backend)
            if line.strip().startswith("backend") and line.strip() == ("backend " + backend):
                flag = True
                continue
            if flag and line.strip().startswith("backend"):
                flag = False
                break
            if flag and line.strip():
                result.append(line)
    return result
def add():
    pass
ret = fetch("www.oldboy.org")
print(ret)
