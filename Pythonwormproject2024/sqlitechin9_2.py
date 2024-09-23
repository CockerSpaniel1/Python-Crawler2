import sqlite3

def entry():
    id1 = input("請輸入欲查詢編號: ")
    sql = "select * from Person where id='%s'" % id1
    connectdb(sql)

def connectdb(sql):
    db = sqlite3.connect("chindb2.db")
    c = db.cursor()
    c.execute(sql)
    result = c.fetchall()
    resultdata(result, c ,db)


def resultdata(result, c ,db):
    for row in result:
            print(row[0]+"\t"+row[1]+"\t"+row[2]+"\t"+row[3]+"\t"+row[4]+"\n")

    c.close()
    db.close()

if __name__=="__main__":
    entry()


# def query():
#     db = sqlite3.connect("chindb2.db")
#     c = db.cursor()
#     sql = "select * from Person"#where id='%s'" % id
#     c.execute(sql)
#     result = c.fetchall()
#     for row in result:
#         print(row[0]+"\t"+row[1]+"\t"+row[2]+"\t"+row[3]+"\t"+row[4]+"\n")
#
#     c.close()
#     db.close()
#
# def write():
#     num = input("請輸入編號: ")
#     name = input("請輸入姓名: ")
#     birth = input("請輸入生日: ")
#     blood = input("請輸入血型: ")
#     edu = input("請輸入學歷: ")
#
#     db = sqlite3.connect("chindb2.db")
#     c = db.cursor()
#     c.execute(f"INSERT INTO person VALUES('{num}', '{name}', '{birth}', '{blood}' , '{edu}')")
#     db.commit()
#     db.close()
#
#
# write()
# query()