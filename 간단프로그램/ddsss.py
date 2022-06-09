import pymssql

conn = pymssql.connect(server='localhost',
                       user='user1',
                       password='rootpass1!!',
                       database='jspdb'
                       )

cursor = conn.cursor()
sql = 'select * from board'
cursor.execute(sql)
rows = cursor.fetchall()
conn.close()

for row in rows:
    print(row)
    # pass