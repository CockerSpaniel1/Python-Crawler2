from pyquery import PyQuery

dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")
links = dom("ul").eq(1).children("li a")
lens1 = len(links)

#
print(lens1)

for i in links.items():
     print(i.text())
