# 基于sqlite3的SQL语句训练

建立本地数据库，轻松实现SQL语句的学习。

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

**一、利用sqlite3包实现SQL语句的执行函数**

```
import sqlite3
import traceback  # 打印错误的详细信息


#  利用sqlite3包实现SQL语句的执行函数
def SQL(sql, db=r'E:\sql_anfany\SQL_anFany.db'):
    '''
    :param sql: 要执行的sql语句
    :param db: 需要连接的数据库
    :return: 执行的sql语句的结果
    '''
    try:
        cn = sqlite3.connect(db)
        c = cn.cursor()
        c.execute(sql)
        print("执行成功")
        cn.commit()
        cn.close()
    except Exception as e:
        print('SQL语句错误：%s' % e)
        print('详细：\n', traceback.format_exc())
```
举例：
1. 创建表
```
sql_create = ''' create table newtable
(
id varchar(255) not null primary key,
name varchar(255) not null,
birthdate date
)
'''
SQL(sql_create)
```

 ![image](https://github.com/Anfany/Python3-Practice/blob/master/sqlite/table.png)
 
2.插入表内容
```
sql_insert = '''insert into newtable
values('001', 'Guido van Rossum', '1956-1-31')
'''
SQL(sql_insert)
```
![image](https://github.com/Anfany/Python3-Practice/blob/master/sqlite/record.png)


**[二、SQL语句经典50题](https://github.com/Anfany/Python3-Practice/blob/master/sqlite/%E7%BB%8F%E5%85%B850.md)**

**三、SQL语句进阶题**
