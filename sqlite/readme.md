# 基于SQLite3的SQL语句训练

安装Python包**sqlite3**，可利用**Anconda**安装。
```
    import sqlite3
    # 打印版本
    print('版本号：%s' % sqlite3.sqlite_version)
```
执行以上语句，不报错，说明安装成功。

**利用sqlite3包实现SQL语句的执行函数**

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
        c.execute(sql)  # 一次执行多条sql语句的函数为executescript,每条语句需以分号结尾
        print("执行成功")
        cn.commit()
        cn.close()
    except Exception as e:
        print('SQL语句错误：%s' % e)
        print('详细：\n', traceback.format_exc())
```
