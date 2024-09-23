from pyquery import PyQuery

dom = PyQuery(url="http://192.168.0.68/Helloproject1/public_html/query3.html", encoding="utf-8")
links = dom("[id='a2#a']")
print(links)

for i in links.items():
    print(i.text())
