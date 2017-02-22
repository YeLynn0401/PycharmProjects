#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 模拟登陆：
# 1. 用户输入帐号密码进行登陆
# 2. 用户信息保存在文件内
# 3. 用户密码输入错误三次后锁定用户
'''
对用户信息文件进行操作的方法
信息数据格式为
{'username': ['password', lock_status,pwd_error_count], ...}
lock_status: int 类型  1、lock 0、unlock 用于手动锁定用户
pwd_error_count ：int 类型 大于2时用户无法登陆
'''
import os
import sys
sys.path.append(os.path.split(os.path.realpath(__file__))[0])


class File_Option():

    def date_read(self, file_name):
        f = open(file_name, 'r', encoding='utf-8')
        date = f.readlines()
        try:
            date = eval(date[0])  # 将文本中内容转化为字典
            # 取出用户信息，添加到user_dic字典中
            # 格式为{username:[pwd,lock,error_count,money]}
        except:
            date = {}
        finally:
            f.close()
            return date  # 返回字典格式用户信息

    def date_write(self, file_name, date):
        status = False
        date_write = str(date)
        f = open(file_name, 'w', encoding='utf-8')
        try:
            f.writelines(date_write)
            f.flush()
            f.close()
            status = True
        finally:
            f.close()
            return status


    def file_read(self):  # 读取文件内容
        file_name = 'user'
        date = self.date_read(file_name)
        return date

    def file_write(self, date):  # 将用户信息字典直接转为字符串覆盖写入到文件中
        file_name = 'user'
        status = self.date_write(file_name, date)
        return status

    def comm_read(self):
        file_name = 'commodity'
        date = self.date_read(file_name)
        return date

    def comm_write(self, date):
        file_name = 'commodity'
        status = self.date_write(file_name, date)
        return status

    def shop_cart_read(self):
        file_name = 'shopping_cart'
        date = self.date_read(file_name)
        return date

    def shop_cart_write(self, date):
        file_name = 'shopping_cart'
        status = self.date_write(file_name, date)
        return status

    def shop_history_read(self):
        file_name = 'shopping_history'
        date = self.date_read(file_name)
        return date

    def shop_history_write(self, date):
        file_name = 'shopping_history'
        status = self.date_write(file_name, date)
        return status

    def money_read(self):
        file_name = 'user_money'
        date = self.date_read(file_name)
        return date

    def money_write(self, date):
        file_name = 'user_money'
        status = self.date_write(file_name, date)
        return status


class user_manage():

    def register(self, name, pwd):
        # 注册方法，需传入：用户名、密码两个参数。返回：成功 或 账号存在
        status = ''
        i = File_Option()
        f = i.file_read()
        fm = i.money_read()
        fs = i.shop_cart_read()
        fh = i.shop_history_read()
        if not f.get(name):  # 初始化用户信息
            f[name] = [pwd, 0, 0, ]   # 初始化密码，lock，error_count
            l = {}
            fm[name] = 0
            i.money_write(fm)  # 初始化余额
            i.file_write(f)
            fs[name] = {}
            fh[name] = []
            i.shop_history_write(fh)
            i.shop_cart_write(fs)  # 初始化购物车

            status = 'success'
        else:
            status = 'exist'
        return status

    def login(self, name, pwd):
        # 传入用户名和密码两个参数，
        # 返回登陆状态值： error 用户名或密码错误，lock 账号已锁定，success 登陆成功
        status = ''
        i = File_Option()
        f = i.file_read()
        user_info = f.get(name)
        if user_info:  # 判断用户名是否存在
            if user_info[1] == 1 or user_info[2] > 2:  # 判断锁定状态
                status = 'lock'
            else:
                if pwd == user_info[0]:  # 判断密码
                    user_info[2] = 0  # 登陆成功，清空密码错误统计
                    f[name] = user_info
                    i.file_write(f)
                    status = 'success'
                else:   # 密码错误，将用户信息文件中登陆错误次数+1
                    user_info[2] += 1
                    f[name] = user_info
                    i.file_write(f)
                    status = 'error'
        else:
            status = 'error'
        return status

    def run(self):
        # 负责打印菜单及根据用户选择调用各函数
        flag = True
        while flag:
            option = input('1、注册\n2、登陆\n3、退出')
            option = option.strip()
            if option == '1':
                flag1 = True
                while flag1:
                    name = input('name:')
                    name = name.strip()
                    pwd = input('pwd:')
                    pwd = pwd.strip()
                    if name and pwd:
                        status = self.register(name, pwd)
                        if status == 'exist':
                            print('用户已经存在')
                        elif status == 'success':
                            print('恭喜注册成功，您的账号为：', name)
                            flag1 = False
                        else:
                            print('error')

                        choice = input('继续请按c，返回上一层应按b，退出请按q：')
                        choice = choice.strip()
                        if choice == 'q':
                            print('bye...')
                            flag = False
                            break

                        elif choice == 'c':
                            pass
                        elif choice == 'b':
                            break
                        else:
                            print('输入有误，bye...')
                            flag = False
                            break
                    else:
                        print('用户名或密码不能为空')


            elif option == '2':
                flag2 = True
                while flag2:
                    name = input('name:')
                    name = name.strip()
                    pwd = input('pwd:')
                    pwd = pwd.strip()
                    if name and pwd:
                        status = self.login(name, pwd)
                        if status == 'error':
                            print('用户名或密码错误')
                        elif status == 'lock':
                            print('账号已经锁定请联系管理员')
                        elif status == 'success':
                            print('登陆成功,welcome:', name)
                            return name
                            exit()
                        else:
                            print('error')
                        choice = input('继续请按c，返回上一层应按b，退出请按q：')
                        choice = choice.strip()
                        if choice == 'q':
                            print('bye...')
                            flag = False
                            break
                        elif choice == 'c':
                            pass
                        elif choice == 'b':
                            break
                        else:
                            print('输入有误，bye...')
                            flag = False
                            break
                    else:
                        print('用户名或密码不能为空')


            elif option == '3':
                flag = False
            else:
                print('error')
        return False

