import sqlite3

connection = sqlite3.connect('test.db')
create_sql = 'create table company(id int primary key not null, emp_name text not null);'
connection.execute(create_sql)
insert_sql = 'insert into company values(?, ?)'
connection.execute(insert_sql, (100, 'LY'))
connection.execute(insert_sql, (200, 'ZW'))

cursors = connection.execute('select id, emp_name from company')
for row in cursors:
    print(row[0], row[1])
connection.close()