#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import pickle


teacher_list = pickle.load(open('teacher', 'rb'))
new_li = list(enumerate(teacher_list))

for i in new_li:
    print(i)
    print(i[0], i[1].name)

print(new_li[2][1])
