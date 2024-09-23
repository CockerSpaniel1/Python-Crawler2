import sqlite3

db = sqlite3.connect("chindb2.db")
c = db.cursor()
c.execute("CREATE TABLE person (id text primary key, name text ,birth text,blood text, school text)")
c.execute("INSERT INTO person VALUES('p1001', '張小玉', '67/12/09', 'A' , '大學')")
db.commit()
db.close()