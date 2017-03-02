## 堡垒机

### 表说明

* host表 主机表[id，ip，端口，主机名]
* hostuser 主机用户表[id，name，pwd，key] 所有主机共用一套密码和key
* hostgroup[id，name] 主机组id和名称
* user [id，name，pwd] 登陆堡垒机的用户信息
* userpermission [id,user_id，host_m2m_hostuser]  用户和主机账户对应表
* host_m2m_hostgroup 主机和主机组的第三张表
* host_m2m_hostuser  主机和主机账户的第三张表
