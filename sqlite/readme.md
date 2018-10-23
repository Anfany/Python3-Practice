# 基于sqlite3的SQL语句训练

建立本地数据库，实现SQL语句的学习。

 1. 安装Python包**sqlite3**，可利用**Anconda**安装。
```
    import sqlite3
    # 打印版本
    print('版本号：%s' % sqlite3.sqlite_version)
```
执行以上语句，不报错，说明安装成功。
 

 2. 安装**Navicat for SQLite**，安装完成后，点击Connection——New SQLite 3，在Database File选择本地的数据库地址。
 
 如图：
 
 ![image](https://github.com/Anfany/Python3-Practice/blob/master/sqlite/db.png)
 
 本地数据库建立完成后
 
 ![image](https://github.com/Anfany/Python3-Practice/blob/master/sqlite/db1.png)
 
 
本项目建立的数据库为SQL_anFany.db，本地的文件储存在E:\sql_anfany。

利用sqlite3包实现SQL语句的执行函数：

举例：
```
import sqlite3

#  利用sqlite3包实现SQL语句的执行函数
def SQL(sql, db=r'E:\sql_anfany\SQL_anFany.db'):
    '''
    :param sql: 要执行的sql语句
    :param db: 需要连接的数据库
    :return: 执行的sql语句的结果
    '''
    cn = sqlite3.connect(db)
    c = cn.cursor()
    c.execute(sql)
    print("执行成功")
    cn.commit()
    cn.close()

sql_create = ''' create table newtable(
id int not null,
name varchar(255) not null,
birthdate data
)
'''
SQL(sql_create)
```
结果：




一、SQL语句：建表



二、SQL语句经典50题
