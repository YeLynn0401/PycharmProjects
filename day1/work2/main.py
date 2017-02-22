
# 三级菜单：
# 1. 运行程序输出第一级菜单
# 2. 选择一级菜单某项，输出二级菜单，同理输出三级菜单
# 3. 菜单数据保存在文件中

f = open('menu.txt', 'r+',encoding= 'utf-8')
date = f.readlines()
info_dic = eval(date[0])


def manage_list(li):  # 接收一个字典，将key取出并添加序号生成列表
    lis = [(key, i) for key, i in enumerate(li)]
    for i in lis:
        for j in i:
            print(j, end=' ')
        print('\n')
    print('q:退出')

    return lis


def option(li,chose):  # 返回下一级必须的key
    return li[int(chose)][1]


def chose(dic):
    while True:
        # 生成大区列表
        lists = manage_list(dic)  # 将字典key 添加序号生成列表
        c = input('输入：')  # 选择key序号
        if not c.isdigit():
            if c == 'q':
                exit()
            elif c == 'b':
                pass
            else:
                print('enter error')
        elif int(c) <= len(lists):
            k = option(lists, c)  # 获取相应key
            new_dict = dic.get(k)  # 根据key取得所包含下一级字典

            while True:
                lists1 = manage_list(new_dict)  # 将字典key 添加序号生成列表
                print('b:返回')
                # print(lists)
                c = input('输入：')  # 选择key序号
                if not c.isdigit():
                    if c == 'q':
                        exit()
                    elif c == 'b':
                        break
                    else:
                        print('enter error')
                elif int(c) <= len(lists1):
                    k = option(lists1, c)  # 获取相应key
                    new_dict1 = new_dict.get(k)  # 根据key取得所包含下一级字典

                    while True:
                        lists2 = manage_list(new_dict1)  # 将字典key 添加序号生成列表
                        print('b:返回')
                        # print(lists)
                        c = input('输入：')  # 选择key序号
                        if not c.isdigit():
                            if c == 'q':
                                exit()
                            elif c == 'b':
                                break
                            else:
                                print('enter error')
                        elif int(c) <= len(lists2):
                            k = option(lists2, c)  # 获取相应key
                            new_dict2 = new_dict1.get(k)  # 根据key取得所包含下一级字典

                            for i in new_dict2:
                                print(i)
                                print('\n')
                            print('b:返回')
                            print('q:退出')
                            x = input('输入：')
                            if x == 'b':
                                pass
                            elif x == 'q':
                                exit()
                            else:
                                print('error')
                        else:
                            print('error')

                else:
                    print('error')
        else:
            print('error')


chose(info_dic)  # 启动程序
