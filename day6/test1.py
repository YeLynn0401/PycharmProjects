#!/usr/bin/env python 
# -*- coding: utf-8 -*-
class A:
    def __init__(self):
        print("A")

    def tt(self):
        print('a.test')


class B:
    def __init__(self):
        print('B')

    def tt(self):
        print('b.test')


class C(A):
    def __init__(self):
        print('C')

    # def tt(self):
    #     print('c.test')


class D(C, B):
    def __init__(self):
        print('D')
d = D()
d.tt()
