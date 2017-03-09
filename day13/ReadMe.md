# 堡垒机

#### 运行 main.py  PS：用户输入框中输入'q'，可返回上一层列表。
### （一）表说明

* host表 主机表[id，ip，port端口，主机名]
* hostuser 主机用户表[id，name，pwd，key] 建议所有主机共用一套密码和key，方便管理
* hostgroup[id，name] 主机组id和名称
* user [id，name，pwd] 登陆堡垒机的用户信息
* userpermission [id,user_id，host_m2m_hostuser]  用户和主机账户对应表
* host_m2m_hostgroup 主机和主机组的第三张表
* host_m2m_hostuser  主机和主机账户的第三张表

### （二）key
* key集中存放在keys文件夹中
* 数据库中可同时存在key和密码，优先使用key，key无法登陆改用密码尝试，对用户透明。

### （三）logs文件
* cmd.log # 记录用户命令
* login.log # 记录用户登陆信息
* ssh.log # paramiko日志

### （四）使用流程

#### 1、管理员选项
* 添加主机
<pre><code>
server_name：server0 # 主机名，随便写
port：22  # 默认 22 可不填
ip ：192.168.100.5  # 主机IP地址，必填
</code></pre>
* 添加服务器账户
<pre>
    <code>
# 密码和key可以二选一，也可以都写，优先使用key，key登陆失败尝试使用密码。
用户名：root  # 可用于登陆主机的用户名
密 码：123456  # 可用于登陆主机的密码
key：key_name  # 可用于登陆主机的key ，只写存放于keys文件夹中的key文件名即可
    </code>
</pre>

* 创建主机组
用于创建主机分组

* 主机关联主机组
将主机添加到主机组中

* 跳板机用户关联主机
给跳板机用户分配权限

* 添加跳板机用户

* 添加服务器账户
添加用于登录服务器的用户名，密码和key

* 主机关联用户名
关联服务器和服务器账号密码

#### 2、用户登陆
输入用户名密码即可登陆，并同时显示可连接的服务器列表，选择id即可登陆。