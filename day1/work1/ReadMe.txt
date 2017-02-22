作业需求：
模拟登陆：
1. 用户输入帐号密码进行登陆
2. 用户信息保存在文件内
3. 用户密码输入错误三次后锁定用户


介绍：
主要文件有两个，main.py（主文件）, user.txt（用户信息文件）


main.py  ：有两个类
    File_Option类负责操作文件
        有file_read，和file_write两个方法分别控制文件读写user.txt文件
        file_read负责取出文件内容，并返回一个字典，内含所有用户信息。
        file_write 接收一个字典，并将字典覆盖写入user.txt中

    user_manage类负责处理交互动作
        有register、login、run三个方法：
            register接收name和pwd两个参数，格式化后存入user.txt中。返回注册成功（success），账号已存在（exist）两个参数
            login：接收name和pwd两个参数，通过与user.txt中内容比较后判断登陆是否成功，返回error 用户名或密码错误，lock 账号已锁定，success 登陆成功三个参数
            run：打印菜单，接收输入，调用其他方法完成流程控制

user.txt  ：存储所有用户信息，格式为：
    {'username': ['password', lock_status,pwd_error_count], ...}

        lock_status: int 类型 初始值为0  1、lock 0、unlock 用于手动锁定用户
        pwd_error_count ：int 类型 记录密码输入错误次数，初始值为0 大于2时用户无法登陆
