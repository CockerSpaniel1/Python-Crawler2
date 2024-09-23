import sqlite3

id1 = input("請輸入查詢編號: ")
db = sqlite3.connect("chindb2.db")
c = db.cursor()
sql = "select * from Person where id='%s'" % id1
c.execute(sql)
result = c.fetchall()
for row in result:
    print(row[0]+"\t"+row[1]+"\t"+row[2]+"\t"+row[3]+"\t"+row[4]+"\n")
# for r in result[0]:
#     print(r, end="\t")
c.close()
db.close()