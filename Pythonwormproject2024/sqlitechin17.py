import sqlite3

db = sqlite3.connect("chindb2.db")
c = db.cursor()
id1 = input("輸入欲刪除編號: ")
sql = "select * from Person where id='%s'" % id1
c.execute(sql)
result = c.fetchall()
len1=len(result)
c.close()
db.close()

if len1!=0:
    for row in result:
        print(row[0] + "\t" + row[1] + "\t" + row[2] + "\t" + row[3] + "\t" + row[4])

    ch = int(input("確認要刪除此筆資料嗎(1)刪除(2)取消:  "))

    if ch == 2:
        quit

    elif ch == 1:
        db2 = sqlite3.connect("chindb2.db")
        c2 = db2.cursor()
        sql = "delete from Person where id='%s'" % id1
        c2.execute(sql)
        db2.commit()
        db2.close()
        print("資料刪除完成")

else:
    print("查無此筆資料")
