#  # -*- coding：utf-8 -*-
# &Author  AnFany

# Python3 连接Sqlserver 数据库

#  引入包
import pymssql

database = '**.***.*.**' #  数据库名字
username = '**'          #  用户名
password = '******'      #  密码
conn = pymssql.connect(database, username, password)  #获取连接
cursor = conn.cursor() # 创建游标
sql = 'SELECT  * FROM *' # SQL语句

cursor.execute(sql)    # 执行语句

for row in cursor:     # 打印结果
    print(row)

cursor.close()      # 关闭游标
conn.close()        # 关闭连接
