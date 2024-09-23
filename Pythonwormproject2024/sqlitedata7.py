from pyquery import PyQuery
import sqlite3

dom = PyQuery(url="https://bugworkshop.blogspot.com/2018/10/diy-esp32esp32_2.html", encoding="utf-8")
links = dom("span")
#lens = len(links)

k=1
p=1
rdata= []
for i in links.items():
    k=k+1
    if (k>=456 and k<=474):
        data = i.text()
        rdata.append(data)
        p+=1


kid=1
iddata = []
fdata = []
kdata = []

len2= len(rdata)
for h in range(0, len2):
    tdata=str(rdata[h]).split("：")
    fdata.append(tdata[0])
    kdata.append(tdata[1])
    sid="com"+str(kid)
    iddata.append(sid)
    kid+=1

len3=len(fdata)

db = sqlite3.connect("chindb26.db")
c = db.cursor()
c.execute("CREATE TABLE espdata (id text primary key, name text ,product text)")
for t in range(0, len3, 1):
    #print(iddata[t] , fdata[t], kdata[t])
    c.execute("INSERT INTO espdata VALUES('"+iddata[t]+"','"+fdata[t]+"','"+kdata[t]+"')")
db.commit()
db.close()



