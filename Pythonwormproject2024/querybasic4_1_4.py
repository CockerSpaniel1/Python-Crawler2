from pyquery import PyQuery

dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")
links = dom(".outer ul li a font")

links2 = dom(".outer ul li a")
len1 = links.length

texts = []
colors = []

hrefs = []

for i in links.items():
    texts.append(i.text())
    colors.append(i.attr.color)
for i in links2.items():
    hrefs.append(i.attr.href)

for i in range(0, len1):
    print(texts[i], colors[i], hrefs[i])
