#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
p =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(p)
from modules.core.file_opt import user_manage,File_Option
from modules.core import card_pay_api, bind_card


def shop():
    # day2拷贝来的商城，添加了信用卡接口，未做其他修改
    user = user_manage()
    name = False
    flag = True
    while True:
        name = user.run()
        if name:
            break
    f = File_Option()
    cart = {}  # 本次购物车列表
    a = f.comm_read()  # 商品列表
    shopping_cart = f.shop_cart_read()  # 购物车列表
    money_dict = f.money_read()
    m = money_dict.get(name)  # 存储余额的变量
    shopping_history = f.shop_history_read()
    while flag:
        print(''.center(29, '-'))
        print('欢迎', name, '来到大卖场,你有', m , '元')
        list1 = [(k, v) for k, v in enumerate(list(a.keys()))]
        for k, v in list1:
            print(k, v)
        print('q 退出')
        print('x 充值')
        print('g 购买历史')
        print('z 绑定信用卡')
        print('c 查看购物车')
        print(''.center(29, '-'))
        c = input('选择：')
        if c == 'z':
            bind_card.bind(name)
        if c == 'x':
            mm = input('输入充值金额：')
            if mm.isdigit() and int(mm) > 0:
                m += int(mm)
                money_dict[name] = m
                status = f.money_write(money_dict)
                if status:
                    print('充值成功，现在余额：', m)
                else:
                    print('充值失败')
                continue
            else:
                print('输入有误')
                continue
        if c == 'g':
            print('---------购物历史------------')
            print('时间\t商品名\t单价\t数量')
            for i in shopping_history.get(name):
                print(i[0])
                for k in i[1]:
                    print(k, i[1][k][0], i[1][k][1])
            print(''.center(29, '-'))
        if c == 'c':
            if shopping_cart.get(name) == {}:
                print('购物车里空空如也，快去添加商品吧。')
            else:
                xcount = 0
                print('------------------购物车-----------------')
                print('名称\t单价\t数量')
                for i in shopping_cart.get(name):
                    xcount += shopping_cart.get(name)[i][0]* shopping_cart.get(name)[i][1]
                    # shopping_cart.get(name)[i][1] 产品数量 i 商品名称
                    print(i, shopping_cart.get(name)[i][0], shopping_cart.get(name)[i][1])
                print(''.center(29, '-'))
                print('共计：', xcount , '元')
                print('选择付款方式1、信用卡 2、商城余额')
                pay = input(':').strip()
                if pay == '1':
                    xcount1 = 0
                    for i in shopping_cart.get(name):
                        # shopping_cart.get(name)[i][1] 产品数量 i 商品名称
                        for x in a:  # 判断库存是否充足
                            for z in a[x]:
                                if i == z:
                                    if a[x][z][1] < shopping_cart.get(name)[i][1]:
                                        shopping_cart[name][i][1] = a[x][z][1]
                                        f.shop_cart_write(shopping_cart)
                                        print('仓库里的', z, '只剩', a[x][z][1], '个了，已将购物车中数量调整为最大库存。')
                        xcount1 += shopping_cart.get(name)[i][0] * shopping_cart.get(name)[i][1]
                    if xcount != xcount1:  # 判断两个价格不一样则说明购物车有调整，重新打印购物车列表
                        xcount = 0
                        print('------------------更新购物车-----------------')
                        for i in shopping_cart.get(name):
                            # 重新统计价格
                            xcount += shopping_cart.get(name)[i][0] * shopping_cart.get(name)[i][1]
                            # shopping_cart.get(name)[i][1] 产品数量 i 商品名称
                            print(i, shopping_cart.get(name)[i][0], shopping_cart.get(name)[i][1])
                        print(''.center(29, '-'))
                        print('共计：', xcount, '元')
                        c1 = input('购物车更新了，确认购买？y/n')
                        c1 = c1.strip()
                        if c1 == 'y':
                            pass
                        else:
                            print('商品还在购物车里等你。')
                            continue
                    ss = card_pay_api.pay(name, xcount)
                    if ss == 'ok':
                        for i in shopping_cart.get(name):
                            for k in a:
                                for v in a[k]:
                                    if i == v:
                                        a[k][v][1] -= shopping_cart.get(name).get(i)[1]
                        f.comm_write(a)  # 刷新库存
                        # 写入一条购物记录
                        log = [time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),
                               shopping_cart.get(name)]
                        shopping_history[name].append(log)
                        f.shop_history_write(shopping_history)  # 购物记录写入完成
                        shopping_cart[name] = {}  # 清空购物车字典
                        f.shop_cart_write(shopping_cart)  # 清空购物车
                        # print('亲爱的：', name, '您的余额为：', m)
                    else:
                        print('扣款失败。')
                elif pay == '2':
                    if m > xcount:
                        buye = input('是否结账y/n?:')
                        buye = buye.strip()
                        if buye == 'y':
                            xcount1 = 0
                            for i in shopping_cart.get(name):
                                # shopping_cart.get(name)[i][1] 产品数量 i 商品名称
                                for x in a:  # 判断库存是否充足
                                    for z in a[x]:
                                        if i == z:
                                            if a[x][z][1] < shopping_cart.get(name)[i][1]:
                                                shopping_cart[name][i][1] = a[x][z][1]
                                                f.shop_cart_write(shopping_cart)
                                                print('仓库里的', z, '只剩', a[x][z][1], '个了，已将购物车中数量调整为最大库存。')
                                xcount1 += shopping_cart.get(name)[i][0] * shopping_cart.get(name)[i][1]
                            if xcount != xcount1:  # 判断两个价格不一样则说明购物车有调整，重新打印购物车列表
                                xcount = 0
                                print('------------------更新购物车-----------------')
                                for i in shopping_cart.get(name):
                                    # 重新统计价格
                                    xcount += shopping_cart.get(name)[i][0] * shopping_cart.get(name)[i][1]
                                    # shopping_cart.get(name)[i][1] 产品数量 i 商品名称
                                    print(i, shopping_cart.get(name)[i][0], shopping_cart.get(name)[i][1])
                                print(''.center(29, '-'))
                                print('共计：', xcount, '元')
                                c1 = input('购物车更新了，确认购买？y/n')
                                c1 = c1.strip()
                                if c1 == 'y':
                                    pass
                                else:
                                    print('商品还在购物车里等你。')
                                    continue
                            m -= xcount
                            print('余额', m)
                            money_dict[name] = m
                            f.money_write(money_dict)  # 以上三条为扣钱
                            for i in shopping_cart.get(name):
                                for k in a:
                                    for v in a[k]:
                                        if i == v:
                                            a[k][v][1] -= shopping_cart.get(name).get(i)[1]
                            f.comm_write(a)  # 刷新库存
                            # 写入一条购物记录
                            log = [time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),
                                   shopping_cart.get(name)]
                            shopping_history[name].append(log)
                            f.shop_history_write(shopping_history)  # 购物记录写入完成
                            shopping_cart[name] = {}  # 清空购物车字典
                            f.shop_cart_write(shopping_cart)  # 清空购物车
                            print('亲爱的：', name, '您的余额为：', m)

                        elif buye == 'n':
                            print('商品还在购物车里等你。')
                        else:
                            print('输入有误。')
                            print('商品还在购物车里等你。')
                    else:
                        print('钱不够了，赚钱去吧少年。')
        if c == 'q':
            print(''.center(29, '-'))
            print('本次购物清单：')
            print('名称\t数量')
            for k in cart:
                print(k, cart.get(k))
                print(''.center(29, '-'))
            print('bye...')
            flag = False
            continue
        if c.isdigit():
            if int(c) < len(list1):
                key1 = list1[int(c)][1]  # 获取选择数字对应的value
                list2 = a.get(key1)
                l = [(k, v) for k, v in enumerate(list(list2.keys()))]  # 商品序号和商品名列表
                print(''.center(29, '-'))
                print('序号 名称 价格 库存')
                for k, v in l:
                    info = list2.get(v)
                    print(k, v, info[0], info[1])
                print(''.center(29, '-'))
                which = input('需要哪个？')
                which = which.strip()
                num = input('数量？')
                num = num.strip()

                if which.isdigit() and num.isdigit():
                    num = int(num)
                    which = int(which)
                    if which < len(l):  # 判断输入是否正确
                        comm_list = list2.get(l[int(which)][1])  # 商品参数列表
                        if num < comm_list[1]:  # 判断库存是否充足
                            if not shopping_cart.get(name).get(l[which][1]):  # 没买过就在购物车字典中添加新商品
                                shopping_cart[name][l[which][1]] = [comm_list[0], num]
                                f.shop_cart_write(shopping_cart)
                            else:  # 购买过就增加商品数量
                                shopping_cart[name][l[which][1]][1] += num
                                f.shop_cart_write(shopping_cart)
                            print( num, '个', l[which][1],'，已经静静的躺在购物车中。')
                        else:
                            print('没有那么多了')
                    else:
                        print('输入有误')

