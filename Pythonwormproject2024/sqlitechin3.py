import sqlite3

db = sqlite3.connect("chindb2.db")
c = db.cursor()
str = "select * from Person"
c.execute(str)
result = c.fetchall()
for row in result:
    print(row[0]+"\t"+row[1]+"\t"+row[2]+"\t"+row[3]+"\t"+row[4]+"\n")

c.close()
db.close()