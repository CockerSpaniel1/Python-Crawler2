import sqlite3

db = sqlite3.connect("chindb1.db")
print("資料庫連線成功")
db.commit()
db.close()