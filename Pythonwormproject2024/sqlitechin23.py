import sqlite3

db = sqlite3.connect("chindb2.db")
c = db.cursor()
sc1 = input("學歷模糊查詢")
sql = f"select * from Person where school like '%{sc1}%'"
c.execute(sql)
result = c.fetchall()

for row in result:
    print(row[0] + "\t" + row[1] + "\t" + row[2] + "\t" + row[3] + "\t" + row[4] + "\n")

c.close()
db.close()


