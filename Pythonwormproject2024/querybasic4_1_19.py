from pyquery import PyQuery

dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")
links = dom(".selectBox").find("#SubCate")
lens = len(links)
print(lens)

dom2=PyQuery(links)
link2 = dom2("select").children("option")
lens2 = len(link2)
print(lens2)

mydata = link2.each(lambda e: e).text()
kdata = mydata.split(" ")
print(kdata)

lens3 = len(kdata)
print(lens3)

for k in range(0, lens3, 1):
    print(kdata[k],k)