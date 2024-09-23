from pyquery import PyQuery

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


fdata = []
kdata = []

len2= len(rdata)
for h in range(0, len2):
    tdata=str(rdata[h]).split("：")
    fdata.append(tdata[0])
    kdata.append(tdata[1])

len3=len(fdata)

for u in range(0, len3, 1):
    print(fdata[u])

print()

for q in range(0, len3, 1):
    print(kdata[q])



