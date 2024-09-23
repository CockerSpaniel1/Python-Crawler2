from pyquery import PyQuery

dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")
links = dom(".outer ul li")
len1 = links.length

# print(len1)
# for h in range(0, len1 ,1):
#      print(links[h].text)

for i in links.items():
    print(i.text())
