import sqlite3

db = sqlite3.connect("chindb2.db")
c = db.cursor()
id1 = input("請輸入查詢編號: ")
sql = "select * from Person where id='%s'" % id1
c.execute(sql)
result = c.fetchall()
print(result)
print(result[0][0])
c.close()
db.close()