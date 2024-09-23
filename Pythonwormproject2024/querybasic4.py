from pyquery import PyQuery

dom = PyQuery(url="http://192.168.0.68/Helloproject1/public_html/query2.html", encoding="utf-8")
links = dom("li")
len1 = links.length
print(len1)
for h in range(0, len1 ,1):
    print(links[h].text)