import sqlite3

db = sqlite3.connect("chindb2.db")
c = db.cursor()
id1 = input("輸入欲修改編號: ")
sql = "select * from Person where id='%s'" % id1
c.execute(sql)
result = c.fetchall()
len1=len(result)
c.close()
db.close()


if len1!=0:
    for row in result:
        ch=input("請選擇(1)"+row[1]+"(2)"+row[2]+"(3)"+row[3]+"(4)"+row[4]+"(5)取消:")
        qname = row[1]
        qbirth = row[2]
        qblood = row[3]
        qschool = row[4]

    if int(ch) == 1:
        newname = input("新姓名: ")
        qname = newname
        sql2 = "update Person set name='"+qname+"' where id='%s'" % id1

    if int(ch) == 2:
        newbirth = input("新生日: ")
        qbirth = newbirth
        sql2 = "update Person set birth='"+qbirth+"' where id='"+id1+"'"

    if int(ch) == 3:
        newblood = input("新血型: ")
        qblood = newblood
        sql2 = "update Person set blood='"+qblood+"' where id='"+id1+"'"

    if int(ch) == 4:
        newschool = input("新學歷: ")
        qschool = newschool
        sql2 = "update Person set school='"+qschool+"' where id='"+id1+"'"

    if int(ch) == 5:
        quit

    if int(ch) != 5:
        db2 = sqlite3.connect("chindb2.db")
        c2 = db2.cursor()
        c2.execute(sql2)
        c2.close()
        db2.commit()
        db2.close()
        print("資料修改成功")
else:
    print("查無此筆資料")


