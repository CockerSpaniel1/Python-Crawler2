import sqlite3

db = sqlite3.connect("chindb2.db")
c = db.cursor()
sql = "select * from Person where id='p1002'"
c.execute(sql)
result = c.fetchall()
len1=len(result)
print(len1)
c.close()
db.close()