#  # -*- coding：utf-8 -*-
# &Author  AnFany

# Python3 连接Oracle数据库

#  引入包
import cx_Oracle  # 导入python链接ORACLE的包

database = '*****'
username = '****'
password = '****'

conn = cx_Oracle.connect(username, password, database)  #获取连接
cursor = conn.cursor() # 获取光标

sql = 'select * from *** t' # 语句

result = cursor.execute(sql) # 执行语句

for row in result:
    print(row)



conn.close()  # 关闭连接
