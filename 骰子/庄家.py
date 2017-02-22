#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import random
import queue
import time
import threading

money_list = []
count_dict = {1: 0,
         2: 0,
         3: 0,
         4: 0,
         5: 0,
         6: 0,
         7: 0,
         }
q = queue.Queue(10)

def kaijiang(a, b, c):
    if a == b == c:
        # print('aaaaa')
        # print(a, b, c, '豹子')
        # baozi += 1
        count_dict[7] += 1
        return 7
    else:
        if a + b + c < 11:
            # da += 1
            return 1
        else:
            #
            return 0


def zhuang():
    flag = True
    while True:
        if q.full():
            # print('full')
            # time.sleep(0.5)
            pass
        else:
            # print('摇了一次骰子')
            a = random.randrange(1, 7)
            b = random.randrange(1, 7)
            c = random.randrange(1, 7)
            d = [a, b, c]
            q.put(d)
            count_dict[a] += 1


def xian():
    i = 0  # 循环次数
    da = 0  # 大
    xiao = 0  # 小
    baozi = 0  # 豹子数量
    money = 10000  # 初始金钱数
    tingshou = 12000
    number = 10000  # 总参与次数
    m = 100  # 每次投注金额
    n = 1  # 当前投注翻倍数
    y = 0  # 0小 1大 7豹子
    while i < number:
        # print(str(i).center(30, '-'))
        x, y = divmod(i, 2)
        # print(x, y)
        # time.sleep(1)
        if money <= 0:
            print('共计', i, '次，把钱输光了')
            break
        elif money > tingshou:
            print('共计', i, '次，赚了：',money)
            return 1
        else:
            date = q.get()

            a = date[0]
            b = date[1]
            c = date[2]
            # print(a, b, c)
            # 投注
            t_money = m * n
            if t_money > money:
                print('不够投注了')
                print('共计', i, '次，赚了：', money)
                break
            # print('投注：', t_money)

            money -= t_money
            # print('还剩:', money)
            result = kaijiang(a, b, c)
            # 统计大小
            if result == 0:
                xiao += 1
            elif result == 1:
                da += 1

            elif result == 7:
                baozi += 1
            else:
                print('err')
            # 判断输赢
            if y == result:
                money += (t_money*2)
                n = 1
                # print('赢了', t_money)
            else:
                # n *= 2
                if n >= 32:
                    n = 1
                else:
                    n *= 2
                # print('输了', t_money)
            i += 1
            money_list.append(money)
        # time.sleep(5)

    print('共计：', i)
    print('大：', '%.2f%%' % (da*100/i))
    print('小：', '%.2f%%' % (xiao*100/i))
    print('豹子：', '%.2f%%' % (baozi*100/i))
    print(i,xiao,da,baozi)

if __name__ == '__main__':

    t1 = threading.Thread(target=zhuang,)
    # t2 = threading.Thread(target=xian, )
    t1.start()
    # t2.start()
    # t2.join()
    xian()
    # print(q.qsize())
    # print(count_dict)
    print('钱最多的时候：', max(money_list))


