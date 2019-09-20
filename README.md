daixijun.mysql
=========

用于快速部署 mysql 集群

支持以下几种集群模式:

* [ ] Primary-Standby 结构
* [x] MGR 单主模式
* [x] MGR 多主模式

环境要求
------------

* Centos 7+
* Ansible 2.8+
* MySQL 8.0+

角色变量
--------------

* **mysql_version**:  mysql 版本(默认 8.0.17)
* **mysql_remote_src**: 是否需要从Ansible 控制机器上复制安装到目标机器,如果需要从网络上下载安装包，请设置为`true`
* **mysql_download_url**: 免安装压缩包下载地址
* **mysql_datadir**: 数据存放目录(默认 /data/mysql)
* **mysql_logdir**: 日志存放目录(默认 /var/log/mysqld)
* **mysql_pidfile**: PID文件位置(默认 /var/run/mysqld/mysqld.pid)
* **mysql_socket**: Socket文件位置(默认 /var/run/mysqld/mysqld.sock)
* **mysql_root_password**: root账号的密码
* **mysql_cluster_type**: 集群类型(默认 mgr) 可选 mgr(Mysql Group Replication)/ms(Master-Slave)
* **mysql_repl_password**: 用于主从/组复制的账号的密码
* **mysql_group_replication_name**: 组复制集群名
* **mysql_group_replication_single_primary_mode**: MGR集群是否为单主模式(默认 true)
* **mysql_databases**: 需要创建的业务数据库
* **mysql_users**: 需要创建的用户

依赖
------------

无

示例
----------------

安装

```shell
ansible-galaxy install daixijun.mysql
```

使用

```yaml
- hosts: servers
  roles:
    - { role: daixijun.mysql, mysql_version: 8.0.17 }
```

License
-------

BSD

TODO
-------

* [  ] 主备架构(Primary-Standby)
<!-- * [ ] mysql_user 模块对于mysql8.0以上的版本，给用户授权`ALL`权限的时候会出现幂等性问题 -->

联系方式
------------------

Xijun Dai <daixijun1990@gmail.com>
