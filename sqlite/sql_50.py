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
        cn = sqlite3.connect(db) # 连接本地数据库
        c = cn.cursor() # 建立游标
        c.executescript(sql) # 一次执行多条sql语句,每条语句后面需要添加分号
        print("执行成功")
        cn.commit() # 提交
        cn.close()  # 关闭游标
    except Exception as e:
        print('SQL语句错误：%s' % e)
        print('详细：\n', traceback.format_exc())

#  学生信息表
create_Student = '''create table Student
(
S varchar(10),
Sname varchar(10),
Sage datetime,
Ssex nvarchar(10)
);
'''
# 添加学生信息
insert_Student = '''
insert into Student (S, Sname, Sage, Ssex)
select '01' , '赵雷' , '1990-01-01' , '男'
union all 
select '02' , '钱电' , '1990-12-21' , '男'
union all 
select '03' , '孙风' , '1990-05-20' , '男'
union all 
select '04' , '李云' , '1990-08-06' , '男'
union all 
select '05' , '周梅' , '1991-12-01' , '女'
union all 
select '06' , '吴兰' , '1992-03-01' , '女'
union all 
select '07' , '郑竹' , '1989-07-01' , '女'
union all 
select '08' , '王菊' , '1990-01-20' , '女';
'''


# 课程信息表
create_Course = '''create table Course
(
C varchar(10),
Cname varchar(10),
T varchar(10)
);
'''
# 添加课程信息
insert_Course = '''insert into Course (C, Cname, T)
select '01' , '语文' , '02'
union all
select '02' , '数学' , '01'
union all
select '03' , '英语' , '03';
'''


# 老师信息表
create_Teacher = '''create table Teacher
(
T varchar(10),
Tname varchar(10)
);
'''
# 添加老师信息
insert_Teacher = '''insert into Teacher (T, Tname)
select '01' , '张三'
union all
select '02' , '李四'
union all
select '03' , '王五';
'''

# 学生成绩表
create_SC = '''create table SC
(
S varchar(10),
C varchar(10),
Score decimal(18,1)
);
'''
# 添加学生成绩
insert_SC = '''insert into SC(S, C, Score)
select '01' , '01' , 80
union all
select '01' , '02' , 90
union all
select '01' , '03' , 99
union all
select '02' , '01' , 70
union all
select '02' , '02' , 60
union all
select '02' , '03' , 80
union all
select '03' , '01' , 80
union all
select '03' , '02' , 80
union all
select '03' , '03' , 80
union all
select '04' , '01' , 50
union all
select '04' , '02' , 30
union all
select '04' , '03' , 20
union all
select '05' , '01' , 76
union all
select '05' , '02' , 87
union all
select '06' , '01' , 31
union all
select '06' , '03' , 34
union all
select '07' , '02' , 89
union all
select '07' , '03' , 98;
'''

# 最终的主程序

if __name__ == '__main__':

    SQL(create_Teacher + create_Student + create_Course + create_SC)  # 创建表

    SQL(insert_Teacher + insert_Student + insert_Course + insert_SC)  # 添加记录

