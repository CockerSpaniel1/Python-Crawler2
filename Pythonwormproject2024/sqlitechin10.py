import sqlite3

flag = True

while flag:
    try:
        i = int(input("選單(1)姓名查詢(2)血型查詢(3)學歷查詢(4)離開:"))

        if i == 4:
            #flag = False
            break

        elif i == 1:
            name = input("請輸入姓名: ")
            sql = "select * from Person where name='%s'" % name

        elif i == 2:
            blood = input("請輸入血型: ")
            sql = "select * from Person where blood='%s'" % blood

        elif i == 3:
            school = input("請輸入學歷: ")
            sql = "select * from Person where school='%s'" % school

        db = sqlite3.connect("chindb2.db")
        c = db.cursor()

        c.execute(sql)
        result = c.fetchall()
        len1 = len(result)

        if len1 !=0:
            for row in result:
                print(row[0]+"\t"+row[1]+"\t"+row[2]+"\t"+row[3]+"\t"+row[4]+"\n")
        else:
            print("查無此筆資料")
        c.close()
        db.close()
    except:
        print("資料型態錯誤---停止運算")
        break
