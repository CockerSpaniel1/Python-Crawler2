import sqlite3

db = sqlite3.connect("chindb2.db")
c = db.cursor()
sql = "select * from Person"
c.execute(sql)
result = c.fetchall()
c.close()
db.close()

leny = len(result)
lenx = len(result[0])
if leny !=0:
    for i in range(0, leny, 1):
        for j in range(0, lenx, 1):
            print(result[i][j], end="\t")
        print()

# for row in result:
#     for item in row:
#         print(item, end="\t")
#     print()

