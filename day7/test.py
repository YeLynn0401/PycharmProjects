#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


class Mydict(dict):

    def __init__(self):
        self.my_key = []
        super(Mydict, self).__init__()

    # def __getitem__(self, item):
    #     super(Mydict, self).__getitem__(item)
    def __setitem__(self, key, value):
        self.my_key.append(key)
        super(Mydict, self).__setitem__(key, value)

    def __str__(self):
        temp = []
        for key in self.my_key:
            value = self.get(key)
            temp.append("'{}':{}".format(key, value))
        super(Mydict, self).__str__()
        ret = '{'+','.join(temp)+'}'
        # print(ret)
        return ret

    def __iter__(self):
        ret = super(Mydict, self).__iter__()
        print(ret)
        return ret
mydict = Mydict()
mydict['w'] = 1
mydict['s'] = 2
print(mydict)
for i in mydict:
    print(mydict[i])
