from pyquery import PyQuery

dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")
links1 = dom("#-1 a")
lens1 = len(links1)
print(lens1)

p=1
for i in links1.items():
     print(p, i.text(), "http://www.photosharp.com.tw/Photosharp/" + i.attr.href)
     p += 1
#
# for i in range(0,lens1 ,1):
#      print(i+1, links1[i].text, "http://www.photosharp.com.tw/Photosharp/"+links1[i].get("href"))
#
