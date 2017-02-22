#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 性别、年龄、工作、人种、国籍、特长，存款。房、车等信息，
import time
import random


class person:
    def __init__(self, sex, age, work, race, nationality, charm=0, speciality=[], money=0, house=[], car=[]):
        self.sex = sex
        self.charm = charm
        self.age = age
        self.work = work
        self.race = race
        self.nationality = nationality
        self.speciality = speciality
        self.money = money
        self.house = house
        self.car = car


John = person('man', 18, 'student', 'yellow', 'Chinese')
Liz = person('woman', 18, 'student', 'write', 'European', 30, ['跳舞', '油画', '流行音乐'])
Peter = person('man',
               25,
               'president',
               'write',
               'American',
               50,
               ['游泳', '足球', '网球', '高尔夫', '写作', '音乐'],
               1000000000,
               ['豪华公寓', '城堡', '海景别墅'],
               ['法拉利', '宾利', '布加迪', '劳斯莱斯', '雷诺', '阿尔法', '凯迪拉克']
               )


def new_run_into():
    print('看到一个人好像Liz啊，要不要去打个招呼？')
    ch = input('1、打招呼\n2、忍者\n').strip()
    if ch == '1':
        if John.money < 30000000:
            print('你：这些年你过的还好么？')
            print('美女：很好，我和Peter已经有了3个孩子，我们正打算去海滨别墅度假，你呢？')
            print('你：.......')
        elif John.money >= 30000000:
            print('你：这些年你过的还好么？')
            time.sleep(1)
            print('Liz：嗯...还好，你呢？')
            time.sleep(1)
            print('你：我也还好，这些年一直坚持学习，手里也有了些积蓄，Peter还好么？')
            time.sleep(1)
            print('Liz：我们已经分手了，他太花心了')
            time.sleep(1)
            print('Liz：其实我还是爱你的，我们还可以重新开始么？')
            time.sleep(1)
            time.sleep(1)
            print('你：抱歉....')
            time.sleep(1)
            print('你：爱过')
            time.sleep(1)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            time.sleep(1)
            print('你放下了过去，英俊的外表下多了几分成熟，通过自己的努力，升任了CEO，迎娶了董事长女儿，走向了人生巅峰')
            time.sleep(1)
            print('恭喜通关')
            print('bye....')
            exit()
    elif ch == '2':
        print('看着Liz离去的背影，不知为何眼泪模糊了双眼。')

def show_info(p):
    print('个人信息'.center(30, '-'))
    print('性别：{}\n年龄：{}\n工作：{}\n人种：{}\n国籍：{}\n特长：{}\n存款：{}\n房子：{}\n车：{}\n魅力值：{}\n'.format(p.sex,
                                                        p.age,
                                                        p.work,
                                                        p.race,
                                                        p.nationality,
                                                        p.speciality,
                                                        p.money,
                                                        p.house,
                                                        p.car,
                                                        p.charm))
    if p.money < 50000000:
        if p.charm > 80:
            if p.sex == 'man':
                print('等级：小王子')
            else:
                print('等级：万人迷')
        elif (p.charm <= 80) and (p.charm > 50):
            if p.sex == 'man':
                print('等级：有魅力')
            else:
                print('等级：超性感')
        elif (p.charm <= 50) and (p.charm > 30):
            if p.sex == 'man':
                print('等级：文艺男')
            else:
                print('等级：文艺女')
        elif p.charm <= 30:
            if p.sex == 'man':
                print('等级：男屌丝')
            else:
                print('等级：女屌丝')
    else:
        if p.charm > 80:
            if p.sex == 'man':
                print('等级：高富帅')
            else:
                print('等级：白富美')
        elif (p.charm <= 80) and (p.charm > 50):
            if p.sex == 'man':
                print('等级：公爵')
            else:
                print('等级：女爵')
        elif (p.charm <= 50) and (p.charm > 30):
            if p.sex == 'man':
                print('等级：绅士')
            else:
                print('等级：淑女')
        elif p.charm <= 30:
            if p.sex == 'man':
                print('等级：土豪')
            else:
                print('等级：富婆')
    print(''.center(30, '-'))


def new_life():
    print('menu'.center(30, '-'))
    print('崭新的一天，干点啥呢？：\n1、打游戏\n2、去工作\n3、睡觉\n4、游泳\n5、打篮球\n6、去学找Alex学开发\nc、查看个人信息')
    print(''.center(30, '-'))
    ch = input().strip()
    if ch == 'c':
        show_info(John)
        return 1
    elif ch == '1':
        John.charm -= 5
        time.sleep(0.5)
        print('打了一天游戏，遇上几个小学生，真无聊')
    elif ch == '2':
        John.charm += 3
        time.sleep(0.5)
        John.money += 100000
        print('工作中的男人最有魅力，钱包也鼓起来了')
    elif ch == '3':
        John.charm -= 3
        time.sleep(0.5)
        print('睡了一天头昏脑胀')
    elif ch == '4':
        time.sleep(0.5)
        if '游泳' in John.speciality:
            John.charm += 5
        else:
            John.speciality.append('游泳')
            print('爱好+1')
        print('游完泳，感觉整个人都精神了')
    elif ch == '5':
        time.sleep(0.5)
        if '打篮球' in John.speciality:
            John.charm += 5
        else:
            John.speciality.append('打篮球')
            print('爱好+1')
        print('打完篮球，感觉屌爆了')
    elif ch == '6':
        time.sleep(0.5)
        if '开发' in John.speciality:
            John.charm += 5
            John.money += 30000000
        else:
            John.speciality.append('开发')
            print('爱好+1')
        print('听了Alex的鸡汤瞬间正能量爆棚，顺便给Alex跑跑腿赚点零花钱。')


def graduate():
    print('\n\n\n\n\n\n\n\n\n')
    print('Loading ......')
    time.sleep(1)
    print('毕业后Liz不满足与和你在一起的生活，机缘巧合下认识了Peter')
    ch = input('是否查看Peter个人信息？y/n\n')
    if ch == 'y':
        show_info(Peter)
    time.sleep(1)
    print('Liz爱上了Peter，要与你分手')
    ch = input('是否挽留？y/n\n')
    if ch == 'y':
        print('你：亲爱的，我们一同经历了那么多美好的时光，可不可以不要离开我？')
        time.sleep(1)
        print('Liz:对不起，我要的生活你给不了.....')
        time.sleep(1)
        print('你：(>﹏<。)～呜呜呜……')
    time.sleep(1)
    print('看到Liz和Peter的背影渐渐远去')
    ch = input('你会选择：\n1、女人千千万，没了咱再换，回家打游戏去\n2、好伤心，先去哭一会儿\n3、爱过就足够了，人生还很长')
    if ch == '1':
        time.sleep(1)
        print('你沉迷游戏，变成了死肥宅')
    elif ch == '2':
        time.sleep(1)
        print('你伤心过度，精神出现了问题')
    elif ch == '3':
        time.sleep(1)
        while True:
            new_life()
            s = random.randrange(13)  # 随机数产生5 ，偶遇女生
            if s == 5:
                new_run_into()


def run_into():
    print('遇到一个女生，心理还有点小激动呢，要不要去打招呼？')
    ch = input('1、打招呼\n2、忍者\n').strip()
    if ch == '1':
        if John.charm < 30:
            print('你：美女，是你掉的砖头么？')
            print('美女：....')
            print('然后就没有然后了')
        elif John.charm > 30:
            print('你：你好，我在那边看到你，感觉不过来打个招呼，以后肯定会后悔。')
            time.sleep(1)
            print('你：我叫John ，请问你叫什么名字？')
            time.sleep(1)
            print('美女：我叫Liz ')
            time.sleep(1)
            print('你利用所看过的《文艺男的自我修养》一书中所传授泡妞技巧，成功和Liz开始了没羞没臊的大学生活')
            time.sleep(1)
            print('大学3年就这么过去了')
            John.age += 3
            Liz.age += 3
            Peter.age += 3
            graduate()
    elif ch == '2':
        print('看着美女离去的背影，一个人凛冽在风中。')


def boring():
    print('菜单'.center(30, '-'))
    print('闲来无聊，干点啥呢？：\n1、打游戏\n2、去上课\n3、睡觉\n4、游泳\n5、打篮球\n6、去图书馆\nc、查看个人信息')
    print(''.center(30, '-'))
    ch = input().strip()
    if ch == 'c':
        show_info(John)
        return 1
    elif ch == '1':
        John.charm -= 5
        time.sleep(0.5)
        print('打了一天游戏，遇上几个小学生，真无聊')
    elif ch == '2':
        John.charm += 3
        time.sleep(0.5)
        print('上了一天课，感觉人生充实了一些')
    elif ch == '3':
        John.charm -= 3
        time.sleep(0.5)
        print('睡了一天头昏脑胀')
    elif ch == '4':

        time.sleep(0.5)
        if '游泳' in John.speciality:
            John.charm += 5
        else:
            John.speciality.append('游泳')
            print('爱好+1')
        print('游完泳，感觉整个人都精神了')
    elif ch == '5':

        time.sleep(0.5)
        if '打篮球' in John.speciality:
            John.charm += 5
        else:
            John.speciality.append('打篮球')
            print('爱好+1')
        print('打完篮球，感觉屌爆了')
    elif ch == '6':

        time.sleep(0.5)
        if '读书' in John.speciality:
            John.charm += 5
        else:
            John.speciality.append('读书')
            print('爱好+1')
        print('读了几本书，感觉棒棒的')
print('嗨 John，欢迎来到游戏人生，快来开启你丰富的生活吧。')
i = 0
while True:
    if i > 15:  # 大学生活有10次机会，魅力值仍低于30的，注定屌丝一生。
        break
    ret = boring()  # 查看个人信息返回1
    r = random.randrange(10)  # 随机数产生5 ，偶遇女生
    if r == 5:
        run_into()
    if ret != 1:
        i += 1

print('由于你的生活实在无趣，已经注定屌丝一生...')
print('bye.....')