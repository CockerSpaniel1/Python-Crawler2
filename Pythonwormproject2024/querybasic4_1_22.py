from pyquery import PyQuery

spath  = "http://www.photosharp.com.tw"
dom = PyQuery(url="http://www.photosharp.com.tw/Photosharp/News2203.html", encoding="utf-8")
links = dom("script")
lens = len(links)

print(lens)

for i in links.items():
    k = i.attr.src
    if (k!=None):
        allpath = spath+i.attr("src")
        print(allpath)

