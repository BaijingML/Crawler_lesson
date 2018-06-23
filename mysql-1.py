import pymysql
'''
db = pymysql.connect(host='localhost', user='root', password='root', port=3306)
cursor = db.cursor()# 使用 cursor() 方法创建一个游标对象 cursor
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()    #获得第一条数据
print('Database version:', data)
cursor.execute("create database spider DEFAULT CHARACTER SET utf8mb4")
db.close()


# 创建一个名为students的数据表
db = pymysql.connect(host='localhost', user='root', password='root', db='spider')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS  students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)
db.close()

# 插入数据
id = '2012001'
user ='Bob'
age = 20
db = pymysql.connect(host='localhost', user='root', password='root',port=3306, db='spider')
cursor = db.cursor()
sql = 'INSERT INTO students(id, user, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit() # 将操作提交到数据库
except:
    db.rollback()
db.close()

# 传入字典来插入数据
db = pymysql.connect(host='localhost', user='root', password='root',port=3306, db='spider')
cursor = db.cursor()
data = {'id':'2012002', 'name':'Tom', 'age':21}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']* len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successfully')
        db.commit()
except:
    print('failed')
    db.rollback()
db.close()

# 主键不存在插入数据，存在则更新数据

db = pymysql.connect(host='localhost', user='root', password='root',port=3306, db='spider')
cursor = db.cursor()
data = {'id':'2012002', 'name':'Tom', 'age':22}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']* len(data))
# ON DUPLICATE KEY UPDATE 若主键已经存在就执行更新操作
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
                                                                                     values=values)
update = ','.join([" {key}=%s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successfully')
        db.commit()
except:
    print('failed')
    db.rollback()
db.close()


# 删除数据
db = pymysql.connect(host='localhost', user='root', password='root',port=3306, db='spider')
cursor = db.cursor()
data = {'id':'2012002', 'name':'Tom', 'age':22}
table = 'students'
condition= 'age > 20'
sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
'''

# 先插入数据再查询数据

db = pymysql.connect(host='localhost', user='root', password='root',port=3306, db='spider')
cursor = db.cursor()
table = 'students'
data = {'id':'2012003', 'name':'Mary', 'age':24}
keys = ','.join(data.keys())
values = ','.join(['%s']* len(data))
# ON DUPLICATE KEY UPDATE 若主键已经存在就执行更新操作
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
                                                                                     values=values)
update = ','.join([" {key}=%s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successfully')
        db.commit()
except:
    print('failed')
    db.rollback()
sql = 'SELECT * FROM students WHERE age > 20'
try:
    cursor.execute(sql)
    print('Cout:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('results:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')









