## SQL基本语法

* 查看数据库：`SHOW DATABASES；`
* 创建数据库：`CREATE DATEBASE 数据库名称；`
* 使用数据库：`USE 数据库名称；`
* 查看数据表：`SHOW TABLES；`
* 创建数据表：`CREATE TABLE 表名称（列名1 （数据类型1），列名2 （数据类型2））；`
* 插入数据：`INSERT INTO 表名称（列名1，列名2） VALUES（数据1，数据2）；`
* 查看数据：`SELECT * FROM 表名称；`
* 更新数据：`UPDATE 表名称 SET 列名1=新数据1，列名2=新数据2 WHERE 某列=某数据；`

## MySQL

**增删改查操作**

```python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:56:15 2020

@author: Administrator
"""

import pymysql 

'''
pymysql使用指南
host = '127.0.0.1' - 回送地址，指本地机
port = 3306        - MySQL的默认端口
user               - 用户名
passwd             - 密码
db                 - 数据库
charset            - 字符类型
'''

# 连接数据库
db = pymysql.connect(host = 'localhost', 
                     user = 'root',  
                     password = 'z19940324',  
                     port = 3306,
                     charset = 'utf8'
                    )
cursor = db.cursor()

# 获取版本号
IN [1]:
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)

OUT[1]: Database version: ('8.0.15',)

# 创建与删除数据库：spiders
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET UTF8MB4")
cursor.execute("drop database if exists spiders")
db.close()

# 创建一个名为 student 的数据表，包含ids、name、age三列，其中age变量类型为int
db = pymysql.connect(host = 'localhost', 
                     user = 'root',  
                     password = 'z19940324',  
                     port = 3306, 
                     db = 'spiders'
                    )
cursor = db.cursor()
sql = ' CREATE TABLE IF NOT EXISTS student(ids VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY(ids))'
cursor.execute(sql)

# 删除创建的 student 的数据表
cursor.execute("drop table if exists student")
db.close()

# 插入数据
ids = '1'
name = 'lei'
age = 15

sql=' INSERT INTO student(ids, name, age) values(%s,%s,%s)'
try:
    cursor.execute(sql,(ids, name, age))
    db.commit()    # 可实现数据插入
    print('成功')
except: 
    db.rollback()  # 执行数据回滚，相当于什么都没有发生过
    print('失败')
    
# 通过字典形式插入数据
data ={'ids': '2',
       'name': 'lei2',
       'age': 19
       }
table = 'student'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(
        table=table,keys=keys,values=values)
try: 
    if cursor.execute(sql,tuple(data.values())): 
        print('Successful')
        db.commit() 
except: 
    print('Failed')
    db.rollback()

# 更新数据
sql=' UPDATE student SET age = %s WHERE name = %s'
try: 
    cursor. execute(sql,(18,'lei'))
    db. commit() 
except: 
    db. rollback()
    print('Failed')

# 如果数据存在，则更新数据；如果数据不存在，则插入数据
data ={'ids': '3',
       'name': 'lei3',
       'age': 20
       }
table = 'student'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(
        table=table,keys=keys,values=values)
update=','.join(["{key} = %s".format(key=key) for key in data])
sql += update

try: 
    if cursor. execute(sql, tuple(data. values())*2):
        print('Successful')
        db.commit() 
except: 
    print('Failed')
    db.rollback()

# 删除数据
table = 'student'
condition = ' age > 19'
sql = ' DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
try: 
    cursor.execute(sql)
    db. commit()
except: 
    print('Failed')
    db.rollback()

# 查询数据
IN [1]:
sql = 'SELECT * FROM student WHERE age >= 10'
try: 
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    one = cursor.fetchone()
    print('One:',one)
    results = cursor.fetchall()
    print('Results:',results)
    print('Results Type:', type(results))
    for row in results: 
        print(row)
except: print('Error')

OUT[1]:
Count: 2
One: ('1', 'lei', 18)
Results: (('2', 'lei2', 19),)
Results Type: <class 'tuple'>
('2', 'lei2', 19)

# 逐条获取数据（推荐该方法）
IN [2]:
sql=' SELECT * FROM student WHERE age >= 10'
try: 
    cursor. execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row: 
        print('Row:', row)
        row = cursor.fetchone()
except: print(' Error')
db.close()

OUT[2]:
Count: 2
Row: ('1', 'lei', 18)
Row: ('2', 'lei2', 19)
```
