import sqlite3

def checkid(id):
    db = sqlite3.connect("chindb2.db")
    c = db.cursor()
    sql = f"select * from Person where id='{id}'"
    c.execute(sql)
    result = c.fetchall()
    len1 = len(result)
    c.close()
    db.close()

    if len1!=0:
        x = True
        #return True
    else:
        x = False
        #return False
    return x


if __name__=="__main__":
    id1 = input("請輸入編號:")
    result2 = checkid(id1)
    if result2:
        print("這筆資料已存在")
    else:
        print("此筆資料不存在")
