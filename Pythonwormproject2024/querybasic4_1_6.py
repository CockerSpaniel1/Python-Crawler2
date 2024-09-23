from pyquery import PyQuery

dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")
links = dom("ul").eq(3)
lens1 = len(links)

dom2=PyQuery(links)
links2= dom("li")
lens2 = len(links2)

print(lens2)


for i in links2.items():
     print(i.text())
