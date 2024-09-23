from pyquery import PyQuery

spath  = "http://www.photosharp.com.tw"
dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")

links = dom("#HotProduct img")
lens = len(links)
print(lens)

for i in links.items():
    k = i.attr("src")
    print(k)

print("---------------------------------------------------")
links = dom("#HotProduct").find("ul").children("li")
for i in links.items():
    img = i.find("img")
    img_src = img.attr.src
    print(i.text())
    print(img_src)
