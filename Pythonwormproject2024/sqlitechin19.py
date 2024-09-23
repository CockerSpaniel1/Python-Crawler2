import sqlite3

while True:
    try:
        ch = int(input("(1)正排序(2)逆排序(3)離開:"))
        if ch == 1:
            sql = "select * from Person order by id asc"

        elif ch == 2:
            sql = "select * from Person order by id desc"

        elif ch == 3:
            break

        db = sqlite3.connect("chindb2.db")
        c = db.cursor()
        c.execute(sql)
        result = c.fetchall()

        for row in result:
            print(row[0] + "\t" + row[1] + "\t" + row[2] + "\t" + row[3] + "\t" + row[4])

        c.close()
        db.close()

    except:
        print("資料型態錯誤---停止運算")


