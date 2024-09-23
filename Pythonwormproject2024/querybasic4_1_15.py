from pyquery import PyQuery

dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")
links = dom("#10").find("a")
lens = len(links)
print(lens)


for i in links.items():
     print(i.text())

